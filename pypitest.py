import httpx

def test():
    r = httpx.get(r'https://www.httpbin.org/get')
    print(r)

if __name__ == '__main__':
    test()
