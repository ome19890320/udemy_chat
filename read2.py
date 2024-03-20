# Line_chat_read
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f :  # -sig 刪除資料類型格式註記
		for line in f :
			lines.append(line.strip())  # strip移除換行符號
	return lines

def convert(lines): # 設計轉換功能

	person = None #其他code null 無效數值表示
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count  =0
	allen_img_count = 0
	viki_img_count  =0
	for line in lines:
		s = line.split(' ') # split 指定 n/空格 則切割 csv 可能是,逗號分割
		time = s[0]
		name = s [1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_img_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_img_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen say', allen_word_count,allen_sticker_count, allen_img_count  )
	print('Viki say',viki_word_count,viki_sticker_count, viki_img_count )




def write_file(filename, lines):
	with open (filename, 'w') as f :
		for line in lines:
			f.write(line + '\n') 

def main():
	lines = read_file('LINE_chat.txt')
	lines = convert(lines)
	# write_file('LINE_output.txt', lines)

main()