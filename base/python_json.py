#coding=utf-8

import json

def main():
	data = [{'a' : 1,'b':2,'c':3,'d':4,'e':5,'f':6}]

	jsonTmp = json.dumps(data,sort_keys=True)
	print(jsonTmp)

	jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}'
	jsonTmp = json.loads(jsonData)
	print(jsonTmp)
	print(jsonTmp['a'],jsonTmp['b'])

if __name__ == "__main__":
	main()