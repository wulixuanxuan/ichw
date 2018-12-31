#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "YuQi Xuan"
__pkuid__  = "1800011787"
__email__  = "1800011787@pku.edu.cn"

"""

import sys
from urllib.request import urlopen
import urllib.error

def wcount(lines, topn=10):
    # 得到出现频率最高的topn个词
    
    words = {}
    wordlist = []
    
    for word in lines.split():
        word = word.strip(""",./;'[]`-=~!@#$%^&*"()_+{}?><'""").lower()
        #删去标点符号 并将大写字母转化为小写
        if word.isalpha():
            words[word] = words.get(word,0) + 1 
    toplist=sorted(words.items(),key=lambda item:item[1],reverse=True)
    if topn > len(words.keys()): # 如果输入的topn大于单词数，则返回所有单词
        topn = len(words.keys())
    for z in toplist[:topn]:
        print ((z[0]+':').ljust(15) +"\t"+ str(z[1]))

if __name__ == '__main__':
    if  len(sys.argv) == 1:      
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:     
        try:    
            doc = urlopen(sys.argv[1])
            content = doc.read().decode("utf-8")
            if len(sys.argv)==2:
                wcount(content)
            else:
                wcount(content,int(sys.argv[2]))
        #提示错误类型
        except urllib.error.URLError:
            print("Sorry,your URL is wrong!")
        except ValueError:
            print("Sorry,you have entered a non-integer for the topn words!") 
        except Exception:
            print("Sorry,an unexpected error has happened!")

