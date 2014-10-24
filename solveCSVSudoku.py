#! /usr/bin/python
import csv
import sys
def solveSudoku(board):
	row=[[False for i in xrange(9)] for i in xrange(9)]
	clm=[[False for i in xrange(9)] for i in xrange(9)]
	blk=[[False for i in xrange(9)] for i in xrange(9)]
	for i in xrange(9):
		for j in xrange(9):
			if board[i][j]!='0':
				c=ord(board[i][j])-ord('1')
				row[i][c]=clm[j][c]=blk[i/3*3+j/3][c]=True
	fill(board,row,clm,blk,0)
def fill(board, row, clm, blk, count):
	while count<81 and board[count/9][count%9]!='0': count+=1
	if count==81: return True
	i=count/9
	j=count%9
	for c in xrange(9):
		if not row[i][c] and not clm[j][c] and not blk[i/3*3+j/3][c]:
			cchar=chr(ord('1')+c)
			board[i][j]=cchar
			row[i][c]=clm[j][c]=blk[i/3*3+j/3][c]=True
			if fill(board,row,clm,blk,count+1): return True
			row[i][c]=clm[j][c]=blk[i/3*3+j/3][c]=False
			board[i][j]='0'
	return False
board=[]
f=open(sys.argv[1],'rb')
outF=open('Solved_'+sys.argv[1],'wb')
try:
	reader=csv.reader(f)
	for row in reader:
		print row
		board.append(row)
	print 'Solving sudoku ...'
	solveSudoku(board)
	writer=csv.writer(outF)
	for line in board: 
		print line 
		writer.writerow(line)
finally:
	f.close()
	outF.close()
