import re
import requests
import sys
from time import sleep
def main():
  try:
    count = 0
    headers = {'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 Mozilla/50.1.0'}
    ans = input("MENU\n1.Search\n2.Copy link\n3.Exit\nEnter your option:")
    if(ans=='1'):
      name = input("Enter the product name:")
      url = 'http://www.amazon.in/s?keywords='+name
      print("Finding the product....")
      htmltext = requests.get(url, headers = headers).text
      out = re.findall(r'data-asin="(.*?)"',htmltext)
      for asin in out[:1]:
        amazon_url = 'http://www.amazon.in/dp/'+asin
      print("Match found")
    elif(ans=='2'):
      amazon_url = input("Enter the URL: ")
    elif(ans=='3'):
      sys.exit()
    else:
      print("Invalid Choice") 
      sys.exit()
    sourceCode = requests.get(amazon_url,headers = headers).text

    try:
      # numb = re.findall(r'<span id="acrCustomerReviewText" class="a-size-base">(.*?) customer reviews</span>',sourceCode)
      # for num1 in numb:
      #  num = int(num1.replace(',',''))
      # rem=num%10
      # if (rem!=0):
      #  r=int(num/10) +1
      # else:
      #  r=num/10
      # if r > 30 : 
      #  r=30
      links = re.findall(r'<a id="acrCustomerReviewLink" class="a-link-normal" href="(.*?)"',sourceCode)
      for link in links[:1]:
       path = re.sub("/ref=.*","",link)
       #print path
      print("Downloading reviews.....")
      file1 = open("new.txt","a")
      file2 = open("new.txt","w")
      try:
        for i in range(1,20):
          pages = 'http://www.amazon.in'+path+'/ref=cm_cr_arp_d_paging_btm_%d?pageNumber=%d'%(i,i)
          linkSource = requests.get(pages,headers = headers).text
          if (count != 0): 
            file = file1
          else: 
            file = file2
            count+=1             
          loi= re.findall(r'<span data-hook="review-body" class="a-size-base review-text">(.*?)</span>',linkSource)
          for lo in loi:
            lo = re.sub('<.*?>','',lo)     
            file.write(lo)
            file.write('\n')
      except Exception as e:
        print(str(e))
    except Exception as e:
      print(str(e))
  except Exception as e:
    print(str(e))

main()

import flip2 as f
f.tokenizeReviews("new.txt","out.txt")

import plot

