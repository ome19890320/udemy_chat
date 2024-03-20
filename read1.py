def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f :  # -sig 刪除資料類型格式註記
		for line in f :
			lines.append(line.strip())  # strip移除換行符號
	return lines

def convert(lines): # 設計轉換功能
	new = [ ]
	person = None #其他code null 無效數值表示
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue # 跳轉至迴圈
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person:
			new. append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open (filename, 'w') as f :
		for line in lines:
			f.write(line + '\n') 

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()