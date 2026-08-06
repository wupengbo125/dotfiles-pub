#!/usr/bin/env python3
import json, os, subprocess, sys, time, urllib.parse, urllib.request

API = 'http://127.0.0.1:9090'
DIR = os.path.expanduser('~/bin/mihomo')

def http(method, path, data=None):
    url = f"{API}{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode()
            return json.loads(content) if content else {}
    except:
        return {}

def test_delay(name):
    enc = urllib.parse.quote('PROXY', safe='')
    http('PUT', f'/proxies/{enc}', {'name': name})
    time.sleep(0.1)
    res = http('GET', f'/proxies/{enc}/delay?timeout=5000&url=http://www.gstatic.com/generate_204')
    return res.get('delay', 9999)

def get_nodes():
    return http('GET', '/providers/proxies/mysub').get('proxies', [])

def start():
    subprocess.run(['sudo', 'pkill', '-f', f'{DIR}/mihomo'], capture_output=True)
    subprocess.run(['rm', '-f', f'{DIR}/sub.yaml'], capture_output=True)
    subprocess.Popen(['sudo', f'{DIR}/mihomo', '-d', DIR],
                     stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    os.system('stty sane 2>/dev/null')

def select(name):
    http('PUT', '/proxies/PROXY', {'name': name})
    print(f'Switched to: {name}')

def test_and_sort(nodes):
    results = []
    for i, p in enumerate(nodes):
        d = test_delay(p['name'])
        results.append((p['name'], d))
        print(f'\r  {i+1}/{len(nodes)} tested', end='', flush=True)
    print()
    results.sort(key=lambda x: (x[1] == 9999, x[1]))
    for i, (name, d) in enumerate(results):
        print(f'{i+1:2d}. {name}  {d if d < 9999 else "timeout"}ms')
    return results

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'default'
    if cmd == 'stop':
        subprocess.run(['sudo', 'pkill', '-f', f'{DIR}/mihomo'])
        return

    # 没传参、或传入 auto / man / list 时，若 API 尚未就绪则启动服务
    nodes = get_nodes()
    if not nodes:
        start()
        print('正在启动...')
        for _ in range(30):
            nodes = get_nodes()
            if nodes and nodes[0].get('name'):
                break
            time.sleep(1)

    if not nodes:
        print('订阅下载失败')
        return

    if cmd == 'list':
        for p in nodes: print(p['name'])
        return

    # 1. 默认无参数模式：找到第一个可用节点，直接切过去并立即结束
    if cmd == 'default':
        ready = None
        for p in nodes:
            d = test_delay(p['name'])
            if d < 9999:
                ready = (p['name'], d)
                break
        if ready:
            select(ready[0])
            print(f'已连接: {ready[0]} ({ready[1]}ms)')
        else:
            print('所有节点都无法连通')
        os.system('stty sane 2>/dev/null')
        return

    # 2. auto 或 man 模式：全量测速
    results = test_and_sort(nodes)
    if cmd == 'auto':
        best = next((name for name, d in results if d < 9999), None)
        if best: select(best)
    elif cmd == 'man':
        c = input('\nSelect node number: ').strip()
        if c.isdigit() and 0 < int(c) <= len(results):
            select(results[int(c)-1][0])

if __name__ == '__main__':
    main()
