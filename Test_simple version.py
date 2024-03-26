import json
import openai
import os
import pandas as pd
from pprint import pprint
import openai
from openai import OpenAI

client = OpenAI()
client = OpenAI(api_key="") #Please set your API KEY. 


#--------------------------------以下是模型选择部分----------------------------------------------
response = client.chat.completions.create(
  #2024/01/25
  model="", #Plesae set your model ID. The model ID can be seen in "train.py"


#-------------------------------以下是测试功能与样本选择部分----------------------------------------- 

  messages=[
    {"role": "system", "content": "You are an BreakGPT."},
  
   #Sample 1: 
   #Right answer for S1-S3: S1 Task: Upward; S2 TASK: 1002.25; S3 TASK: Sell

   #S1:
   #{"role": "user", "content": "Table 0: Sell Buy Price 22 60 1001.75 96 84 1001.50 15 71 1001.25 57 157 1001.00 95 104 1000.75 255 266 1000.50 280 241 1000.25 77 0 1000.00 Table 1: Sell Buy Price 48 137 1002.00 219 201 1001.75 289 243 1001.50 36 0 1001.25 Table 2: Sell Buy Price 62 37 1001.50 197 271 1001.25 294 267 1001.00 108 116 1000.75 9 0 1000.50 Table 3: Sell Buy Price 0 83 1001.75 168 364 1001.50 295 359 1001.25 112 50 1001.00 72 54 1000.75 53 12 1000.50 61 5 1000.25 59 9 1000.00 Table 4: Sell Buy Price 74 212 1001.25 141 82 1001.00 154 159 1000.75 186 299 1000.50 208 219 1000.25 64 10 1000.00 Table 5: Sell Buy Price 0 4 1001.75 16 63 1001.50 113 178 1001.25 235 175 1001.00 119 173 1000.75 46 52 1000.50 Table 6: Sell Buy Price 39 110 1001.75 160 222 1001.50 211 231 1001.25 181 98 1001.00 9 0 1000.75 Table 7: Sell Buy Price 0 13 1001.75 231 202 1001.50 291 241 1001.25 134 105 1001.00 11 0 1000.75 Table 8: Sell Buy Price 3 27 1001.50 147 154 1001.25 315 336 1001.00 131 85 1000.75 123 37 1000.50 Table 9: Sell Buy Price 12 147 1002.25 161 347 1002.00 309 280 1001.75 170 133 1001.50 83 93 1001.25 48 27 1001.00 Table 10: Sell Buy Price 46 215 1002.75 366 200 1002.50 60 142 1002.25 205 228 1002.00 66 55 1001.75 Now you're an expert in stock breakout detection. What is the direction of the breakout based on given tables? Please give reason to the answer firstly, and then answer ”upward ” or “downward”."}
   #S2
   #{"role": "user", "content": "Table 0: Sell Buy Price 22 60 1001.75 96 84 1001.50 15 71 1001.25 57 157 1001.00 95 104 1000.75 255 266 1000.50 280 241 1000.25 77 0 1000.00 Table 1: Sell Buy Price 48 137 1002.00 219 201 1001.75 289 243 1001.50 36 0 1001.25 Table 2: Sell Buy Price 62 37 1001.50 197 271 1001.25 294 267 1001.00 108 116 1000.75 9 0 1000.50 Table 3: Sell Buy Price 0 83 1001.75 168 364 1001.50 295 359 1001.25 112 50 1001.00 72 54 1000.75 53 12 1000.50 61 5 1000.25 59 9 1000.00 Table 4: Sell Buy Price 74 212 1001.25 141 82 1001.00 154 159 1000.75 186 299 1000.50 208 219 1000.25 64 10 1000.00 Table 5: Sell Buy Price 0 4 1001.75 16 63 1001.50 113 178 1001.25 235 175 1001.00 119 173 1000.75 46 52 1000.50 Table 6: Sell Buy Price 39 110 1001.75 160 222 1001.50 211 231 1001.25 181 98 1001.00 9 0 1000.75 Table 7: Sell Buy Price 0 13 1001.75 231 202 1001.50 291 241 1001.25 134 105 1001.00 11 0 1000.75 Table 8: Sell Buy Price 3 27 1001.50 147 154 1001.25 315 336 1001.00 131 85 1000.75 123 37 1000.50 Table 9: Sell Buy Price 12 147 1002.25 161 347 1002.00 309 280 1001.75 170 133 1001.50 83 93 1001.25 48 27 1001.00 Table 10: Sell Buy Price 46 215 1002.75 366 200 1002.50 60 142 1002.25 205 228 1002.00 66 55 1001.75 Now you're an expert in stock breakout detection. Now you're an expert in stock breakout detection. The direction of the breakout is upward. What is the resistance level based on given tables? Please give reason to the answer firstly, and then answer the question."}
   #S3:
   #{"role": "user", "content": "Table 0: Sell Buy Price 22 60 1001.75 96 84 1001.50 15 71 1001.25 57 157 1001.00 95 104 1000.75 255 266 1000.50 280 241 1000.25 77 0 1000.00 Table 1: Sell Buy Price 48 137 1002.00 219 201 1001.75 289 243 1001.50 36 0 1001.25 Table 2: Sell Buy Price 62 37 1001.50 197 271 1001.25 294 267 1001.00 108 116 1000.75 9 0 1000.50 Table 3: Sell Buy Price 0 83 1001.75 168 364 1001.50 295 359 1001.25 112 50 1001.00 72 54 1000.75 53 12 1000.50 61 5 1000.25 59 9 1000.00 Table 4: Sell Buy Price 74 212 1001.25 141 82 1001.00 154 159 1000.75 186 299 1000.50 208 219 1000.25 64 10 1000.00 Table 5: Sell Buy Price 0 4 1001.75 16 63 1001.50 113 178 1001.25 235 175 1001.00 119 173 1000.75 46 52 1000.50 Table 6: Sell Buy Price 39 110 1001.75 160 222 1001.50 211 231 1001.25 181 98 1001.00 9 0 1000.75 Table 7: Sell Buy Price 0 13 1001.75 231 202 1001.50 291 241 1001.25 134 105 1001.00 11 0 1000.75 Table 8: Sell Buy Price 3 27 1001.50 147 154 1001.25 315 336 1001.00 131 85 1000.75 123 37 1000.50 Table 9: Sell Buy Price 12 147 1002.25 161 347 1002.00 309 280 1001.75 170 133 1001.50 83 93 1001.25 48 27 1001.00 Table 10: Sell Buy Price 46 215 1002.75 366 200 1002.50 60 142 1002.25 205 228 1002.00 66 55 1001.75 Now you're an expert in stock breakout detection. The direction of the breakout is upward. The resistance level is 1002.25. In terms of the number of orders, which side (buyer/seller) has more orders above the resistance level? Please give reason to the answer firstly, and then answer the question."} 
   #Testing the model without Multi-stage structure. Please change the model ID to the trained model without Multi-stage structure and test this task:
   #{"role": "user", "content": "Table 0: Sell Buy Price 22 60 1001.75 96 84 1001.50 15 71 1001.25 57 157 1001.00 95 104 1000.75 255 266 1000.50 280 241 1000.25 77 0 1000.00 Table 1: Sell Buy Price 48 137 1002.00 219 201 1001.75 289 243 1001.50 36 0 1001.25 Table 2: Sell Buy Price 62 37 1001.50 197 271 1001.25 294 267 1001.00 108 116 1000.75 9 0 1000.50 Table 3: Sell Buy Price 0 83 1001.75 168 364 1001.50 295 359 1001.25 112 50 1001.00 72 54 1000.75 53 12 1000.50 61 5 1000.25 59 9 1000.00 Table 4: Sell Buy Price 74 212 1001.25 141 82 1001.00 154 159 1000.75 186 299 1000.50 208 219 1000.25 64 10 1000.00 Table 5: Sell Buy Price 0 4 1001.75 16 63 1001.50 113 178 1001.25 235 175 1001.00 119 173 1000.75 46 52 1000.50 Table 6: Sell Buy Price 39 110 1001.75 160 222 1001.50 211 231 1001.25 181 98 1001.00 9 0 1000.75 Table 7: Sell Buy Price 0 13 1001.75 231 202 1001.50 291 241 1001.25 134 105 1001.00 11 0 1000.75 Table 8: Sell Buy Price 3 27 1001.50 147 154 1001.25 315 336 1001.00 131 85 1000.75 123 37 1000.50 Table 9: Sell Buy Price 12 147 1002.25 161 347 1002.00 309 280 1001.75 170 133 1001.50 83 93 1001.25 48 27 1001.00 Table 10: Sell Buy Price 46 215 1002.75 366 200 1002.50 60 142 1002.25 205 228 1002.00 66 55 1001.75 Now you're an expert in stock breakout detection. Do you think the stock in the picture will have a true breakout based on given tables? Please give reason to the answer firstly, and then answer” It is a true breakout” or “It is a false breakout”."}
   #Testing Final report(rational + final answer). Please change the model ID to trained report generator and test this task:
   #{"role": "user", "content": "Table 0: Sell Buy Price 22 60 1001.75 96 84 1001.50 15 71 1001.25 57 157 1001.00 95 104 1000.75 255 266 1000.50 280 241 1000.25 77 0 1000.00 Table 1: Sell Buy Price 48 137 1002.00 219 201 1001.75 289 243 1001.50 36 0 1001.25 Table 2: Sell Buy Price 62 37 1001.50 197 271 1001.25 294 267 1001.00 108 116 1000.75 9 0 1000.50 Table 3: Sell Buy Price 0 83 1001.75 168 364 1001.50 295 359 1001.25 112 50 1001.00 72 54 1000.75 53 12 1000.50 61 5 1000.25 59 9 1000.00 Table 4: Sell Buy Price 74 212 1001.25 141 82 1001.00 154 159 1000.75 186 299 1000.50 208 219 1000.25 64 10 1000.00 Table 5: Sell Buy Price 0 4 1001.75 16 63 1001.50 113 178 1001.25 235 175 1001.00 119 173 1000.75 46 52 1000.50 Table 6: Sell Buy Price 39 110 1001.75 160 222 1001.50 211 231 1001.25 181 98 1001.00 9 0 1000.75 Table 7: Sell Buy Price 0 13 1001.75 231 202 1001.50 291 241 1001.25 134 105 1001.00 11 0 1000.75 Table 8: Sell Buy Price 3 27 1001.50 147 154 1001.25 315 336 1001.00 131 85 1000.75 123 37 1000.50 Table 9: Sell Buy Price 12 147 1002.25 161 347 1002.00 309 280 1001.75 170 133 1001.50 83 93 1001.25 48 27 1001.00 Table 10: Sell Buy Price 46 215 1002.75 366 200 1002.50 60 142 1002.25 205 228 1002.00 66 55 1001.75 Now you're an expert in stock breakout detection. The direction of the breakout is upward. The resistance level is 1002.25.The seller side has more orders above the resistance level. Analyze whether this is a true or false breakout based on the known conditions, and give reasons."}
  
  #Sample 2: 
  #Right answer for S1-S3: S1 Task: Downward; S2 TASK: 1005.75; S3 TASK: Sell

   #S1:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 48 1007.25 19 51 1007.00 1 0 1006.75 Table 1: Sell Buy Price 0 19 1007.75 37 65 1007.50 9 0 1007.25 Table 2: Sell Buy Price 0 23 1008.00 54 90 1007.75 33 34 1007.50 2 0 1007.25 Table 3: Sell Buy Price 0 4 1008.25 61 55 1008.00 37 0 1007.75 52 72 1007.50 24 0 1007.25 Table 4: Sell Buy Price 0 18 1007.75 27 17 1007.50 Table 5: Sell Buy Price 0 3 1007.75 46 3 1007.50 29 0 1007.25 129 114 1007.00 14 0 1006.75 Table 6: Sell Buy Price 0 1 1007.00 70 39 1006.75 58 0 1006.50 Table 7: Sell Buy Price 107 159 1006.50 70 54 1006.25 67 5 1006.00 Table 8: Sell Buy Price 0 5 1006.50 53 66 1006.25 71 85 1006.00 23 0 1005.75 Table 9: Sell Buy Price 33 99 1006.25 65 30 1006.00 Table 10: Sell Buy Price 0 19 1006.25 39 1 1006.00 82 20 1005.75 139 116 1005.50 96 2 1005.25 111 34 1005.00 120 67 1004.75 28 0 1004.50 Now you're an expert in stock breakout detection. What is the direction of the breakout based on given tables? Please give reason to the answer firstly, and then answer ”upward ” or “downward”."}
   #S2:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 48 1007.25 19 51 1007.00 1 0 1006.75 Table 1: Sell Buy Price 0 19 1007.75 37 65 1007.50 9 0 1007.25 Table 2: Sell Buy Price 0 23 1008.00 54 90 1007.75 33 34 1007.50 2 0 1007.25 Table 3: Sell Buy Price 0 4 1008.25 61 55 1008.00 37 0 1007.75 52 72 1007.50 24 0 1007.25 Table 4: Sell Buy Price 0 18 1007.75 27 17 1007.50 Table 5: Sell Buy Price 0 3 1007.75 46 3 1007.50 29 0 1007.25 129 114 1007.00 14 0 1006.75 Table 6: Sell Buy Price 0 1 1007.00 70 39 1006.75 58 0 1006.50 Table 7: Sell Buy Price 107 159 1006.50 70 54 1006.25 67 5 1006.00 Table 8: Sell Buy Price 0 5 1006.50 53 66 1006.25 71 85 1006.00 23 0 1005.75 Table 9: Sell Buy Price 33 99 1006.25 65 30 1006.00 Table 10: Sell Buy Price 0 19 1006.25 39 1 1006.00 82 20 1005.75 139 116 1005.50 96 2 1005.25 111 34 1005.00 120 67 1004.75 28 0 1004.50 Now you're an expert in stock breakout detection. Now you're an expert in stock breakout detection. The direction of the breakout is downward. What is the resistance level based on given tables? Please give reason to the answer firstly, and then answer the question."}
   #S3:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 48 1007.25 19 51 1007.00 1 0 1006.75 Table 1: Sell Buy Price 0 19 1007.75 37 65 1007.50 9 0 1007.25 Table 2: Sell Buy Price 0 23 1008.00 54 90 1007.75 33 34 1007.50 2 0 1007.25 Table 3: Sell Buy Price 0 4 1008.25 61 55 1008.00 37 0 1007.75 52 72 1007.50 24 0 1007.25 Table 4: Sell Buy Price 0 18 1007.75 27 17 1007.50 Table 5: Sell Buy Price 0 3 1007.75 46 3 1007.50 29 0 1007.25 129 114 1007.00 14 0 1006.75 Table 6: Sell Buy Price 0 1 1007.00 70 39 1006.75 58 0 1006.50 Table 7: Sell Buy Price 107 159 1006.50 70 54 1006.25 67 5 1006.00 Table 8: Sell Buy Price 0 5 1006.50 53 66 1006.25 71 85 1006.00 23 0 1005.75 Table 9: Sell Buy Price 33 99 1006.25 65 30 1006.00 Table 10: Sell Buy Price 0 19 1006.25 39 1 1006.00 82 20 1005.75 139 116 1005.50 96 2 1005.25 111 34 1005.00 120 67 1004.75 28 0 1004.50 Now you're an expert in stock breakout detection. The direction of the breakout is downward. The resistance level is 1005.75. In terms of the number of orders, which side (buyer/seller) has more orders above the resistance level? Please give reason to the answer firstly, and then answer the question."} 
   #Testing the model without Multi-stage structure. Please change the model ID to the trained model without Multi-stage structure and test this task:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 48 1007.25 19 51 1007.00 1 0 1006.75 Table 1: Sell Buy Price 0 19 1007.75 37 65 1007.50 9 0 1007.25 Table 2: Sell Buy Price 0 23 1008.00 54 90 1007.75 33 34 1007.50 2 0 1007.25 Table 3: Sell Buy Price 0 4 1008.25 61 55 1008.00 37 0 1007.75 52 72 1007.50 24 0 1007.25 Table 4: Sell Buy Price 0 18 1007.75 27 17 1007.50 Table 5: Sell Buy Price 0 3 1007.75 46 3 1007.50 29 0 1007.25 129 114 1007.00 14 0 1006.75 Table 6: Sell Buy Price 0 1 1007.00 70 39 1006.75 58 0 1006.50 Table 7: Sell Buy Price 107 159 1006.50 70 54 1006.25 67 5 1006.00 Table 8: Sell Buy Price 0 5 1006.50 53 66 1006.25 71 85 1006.00 23 0 1005.75 Table 9: Sell Buy Price 33 99 1006.25 65 30 1006.00 Table 10: Sell Buy Price 0 19 1006.25 39 1 1006.00 82 20 1005.75 139 116 1005.50 96 2 1005.25 111 34 1005.00 120 67 1004.75 28 0 1004.50 Now you're an expert in stock breakout detection. Do you think the stock in the picture will have a true breakout based on given tables? Please give reason to the answer firstly, and then answer” It is a true breakout” or “It is a false breakout”."} 
   #Testing Final report(rational + final answer). Please change the model ID to trained report generator and test this task:
   #{"role": "user", "content": " Now you're an expert in stock breakout detection. The direction of the breakout is downward. The resistance level is 1005.75.The seller side has more orders above the resistance level. Analyze whether this is a true or false breakout based on the known conditions, and give reasons."}

#Sample 3: 
  #Right answer for S1-S3: S1 Task: Upward; S2 TASK: 1005.25; S3 TASK: Buy

   #S1:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 144 1004.75 54 88 1004.50 118 108 1004.25 57 67 1004.00 162 136 1003.75 89 33 1003.50 Table 1: Sell Buy Price 3 83 1005.00 329 179 1004.75 118 135 1004.50 158 154 1004.25 23 0 1004.00 Table 2: Sell Buy Price 81 177 1005.25 169 218 1005.00 202 124 1004.75 118 127 1004.50 225 223 1004.25 130 65 1004.00 Table 3: Sell Buy Price 38 62 1004.50 162 270 1004.25 47 30 1004.00 97 45 1003.75 18 49 1003.50 243 139 1003.25 163 64 1003.00 53 21 1002.75 Table 4: Sell Buy Price 0 42 1003.75 346 256 1003.50 248 228 1003.25 126 55 1003.00 102 47 1002.75 74 37 1002.50 47 0 1002.25 Table 5: Sell Buy Price 44 62 1004.00 92 119 1003.75 171 128 1003.50 23 47 1003.25 112 113 1003.00 63 40 1002.75 20 55 1002.50 8 0 1002.25 Table 6: Sell Buy Price 0 4 1004.25 72 102 1004.00 164 226 1003.75 186 190 1003.50 102 22 1003.25 Table 7: Sell Buy Price 0 12 1005.00 93 173 1004.75 171 162 1004.50 188 148 1004.25 68 47 1004.00 85 136 1003.75 39 29 1003.50 41 26 1003.25 50 35 1003.00 11 0 1002.75 Table 8: Sell Buy Price 0 16 1003.50 62 66 1003.25 197 147 1003.00 421 383 1002.75 152 49 1002.50 1 0 1002.25 Table 9: Sell Buy Price 15 48 1005.00 137 222 1004.75 115 212 1004.50 65 209 1004.25 42 112 1004.00 196 137 1003.75 138 114 1003.50 32 15 1003.25 12 32 1003.00 Table 10: Sell Buy Price 0 21 1008.25 489 537 1008.00 361 264 1007.75 50 256 1007.50 202 539 1007.25 230 335 1007.00 96 248 1006.75 24 190 1006.50 14 152 1006.25 0 125 1006.00 3 196 1005.75 8 78 1005.50 5 58 1005.25 54 163 1005.00 341 182 1004.75 1 0 1004.50 Now you're an expert in stock breakout detection. What is the direction of the breakout based on given tables? Please give reason to the answer firstly, and then answer ”upward ” or “downward”."}
   #S2:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 144 1004.75 54 88 1004.50 118 108 1004.25 57 67 1004.00 162 136 1003.75 89 33 1003.50 Table 1: Sell Buy Price 3 83 1005.00 329 179 1004.75 118 135 1004.50 158 154 1004.25 23 0 1004.00 Table 2: Sell Buy Price 81 177 1005.25 169 218 1005.00 202 124 1004.75 118 127 1004.50 225 223 1004.25 130 65 1004.00 Table 3: Sell Buy Price 38 62 1004.50 162 270 1004.25 47 30 1004.00 97 45 1003.75 18 49 1003.50 243 139 1003.25 163 64 1003.00 53 21 1002.75 Table 4: Sell Buy Price 0 42 1003.75 346 256 1003.50 248 228 1003.25 126 55 1003.00 102 47 1002.75 74 37 1002.50 47 0 1002.25 Table 5: Sell Buy Price 44 62 1004.00 92 119 1003.75 171 128 1003.50 23 47 1003.25 112 113 1003.00 63 40 1002.75 20 55 1002.50 8 0 1002.25 Table 6: Sell Buy Price 0 4 1004.25 72 102 1004.00 164 226 1003.75 186 190 1003.50 102 22 1003.25 Table 7: Sell Buy Price 0 12 1005.00 93 173 1004.75 171 162 1004.50 188 148 1004.25 68 47 1004.00 85 136 1003.75 39 29 1003.50 41 26 1003.25 50 35 1003.00 11 0 1002.75 Table 8: Sell Buy Price 0 16 1003.50 62 66 1003.25 197 147 1003.00 421 383 1002.75 152 49 1002.50 1 0 1002.25 Table 9: Sell Buy Price 15 48 1005.00 137 222 1004.75 115 212 1004.50 65 209 1004.25 42 112 1004.00 196 137 1003.75 138 114 1003.50 32 15 1003.25 12 32 1003.00 Table 10: Sell Buy Price 0 21 1008.25 489 537 1008.00 361 264 1007.75 50 256 1007.50 202 539 1007.25 230 335 1007.00 96 248 1006.75 24 190 1006.50 14 152 1006.25 0 125 1006.00 3 196 1005.75 8 78 1005.50 5 58 1005.25 54 163 1005.00 341 182 1004.75 1 0 1004.50 Now you're an expert in stock breakout detection. Now you're an expert in stock breakout detection. The direction of the breakout is upward. What is the resistance level based on given tables? Please give reason to the answer firstly, and then answer the question."}
   #S3:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 144 1004.75 54 88 1004.50 118 108 1004.25 57 67 1004.00 162 136 1003.75 89 33 1003.50 Table 1: Sell Buy Price 3 83 1005.00 329 179 1004.75 118 135 1004.50 158 154 1004.25 23 0 1004.00 Table 2: Sell Buy Price 81 177 1005.25 169 218 1005.00 202 124 1004.75 118 127 1004.50 225 223 1004.25 130 65 1004.00 Table 3: Sell Buy Price 38 62 1004.50 162 270 1004.25 47 30 1004.00 97 45 1003.75 18 49 1003.50 243 139 1003.25 163 64 1003.00 53 21 1002.75 Table 4: Sell Buy Price 0 42 1003.75 346 256 1003.50 248 228 1003.25 126 55 1003.00 102 47 1002.75 74 37 1002.50 47 0 1002.25 Table 5: Sell Buy Price 44 62 1004.00 92 119 1003.75 171 128 1003.50 23 47 1003.25 112 113 1003.00 63 40 1002.75 20 55 1002.50 8 0 1002.25 Table 6: Sell Buy Price 0 4 1004.25 72 102 1004.00 164 226 1003.75 186 190 1003.50 102 22 1003.25 Table 7: Sell Buy Price 0 12 1005.00 93 173 1004.75 171 162 1004.50 188 148 1004.25 68 47 1004.00 85 136 1003.75 39 29 1003.50 41 26 1003.25 50 35 1003.00 11 0 1002.75 Table 8: Sell Buy Price 0 16 1003.50 62 66 1003.25 197 147 1003.00 421 383 1002.75 152 49 1002.50 1 0 1002.25 Table 9: Sell Buy Price 15 48 1005.00 137 222 1004.75 115 212 1004.50 65 209 1004.25 42 112 1004.00 196 137 1003.75 138 114 1003.50 32 15 1003.25 12 32 1003.00 Table 10: Sell Buy Price 0 21 1008.25 489 537 1008.00 361 264 1007.75 50 256 1007.50 202 539 1007.25 230 335 1007.00 96 248 1006.75 24 190 1006.50 14 152 1006.25 0 125 1006.00 3 196 1005.75 8 78 1005.50 5 58 1005.25 54 163 1005.00 341 182 1004.75 1 0 1004.50 Now you're an expert in stock breakout detection. The direction of the breakout is upward. The resistance level is 1005.25. In terms of the number of orders, which side (buyer/seller) has more orders above the resistance level? Please give reason to the answer firstly, and then answer the question."} 
   #Testing the model without Multi-stage structure. Please change the model ID to the trained model without Multi-stage structure and test this task:
   #{"role": "user", "content": "Table 0: Sell Buy Price 0 144 1004.75 54 88 1004.50 118 108 1004.25 57 67 1004.00 162 136 1003.75 89 33 1003.50 Table 1: Sell Buy Price 3 83 1005.00 329 179 1004.75 118 135 1004.50 158 154 1004.25 23 0 1004.00 Table 2: Sell Buy Price 81 177 1005.25 169 218 1005.00 202 124 1004.75 118 127 1004.50 225 223 1004.25 130 65 1004.00 Table 3: Sell Buy Price 38 62 1004.50 162 270 1004.25 47 30 1004.00 97 45 1003.75 18 49 1003.50 243 139 1003.25 163 64 1003.00 53 21 1002.75 Table 4: Sell Buy Price 0 42 1003.75 346 256 1003.50 248 228 1003.25 126 55 1003.00 102 47 1002.75 74 37 1002.50 47 0 1002.25 Table 5: Sell Buy Price 44 62 1004.00 92 119 1003.75 171 128 1003.50 23 47 1003.25 112 113 1003.00 63 40 1002.75 20 55 1002.50 8 0 1002.25 Table 6: Sell Buy Price 0 4 1004.25 72 102 1004.00 164 226 1003.75 186 190 1003.50 102 22 1003.25 Table 7: Sell Buy Price 0 12 1005.00 93 173 1004.75 171 162 1004.50 188 148 1004.25 68 47 1004.00 85 136 1003.75 39 29 1003.50 41 26 1003.25 50 35 1003.00 11 0 1002.75 Table 8: Sell Buy Price 0 16 1003.50 62 66 1003.25 197 147 1003.00 421 383 1002.75 152 49 1002.50 1 0 1002.25 Table 9: Sell Buy Price 15 48 1005.00 137 222 1004.75 115 212 1004.50 65 209 1004.25 42 112 1004.00 196 137 1003.75 138 114 1003.50 32 15 1003.25 12 32 1003.00 Table 10: Sell Buy Price 0 21 1008.25 489 537 1008.00 361 264 1007.75 50 256 1007.50 202 539 1007.25 230 335 1007.00 96 248 1006.75 24 190 1006.50 14 152 1006.25 0 125 1006.00 3 196 1005.75 8 78 1005.50 5 58 1005.25 54 163 1005.00 341 182 1004.75 1 0 1004.50 Now you're an expert in stock breakout detection. Do you think the stock in the picture will have a true breakout based on given tables? Please give reason to the answer firstly, and then answer” It is a true breakout” or “It is a false breakout”."}
   #Testing Final report(rational + final answer). Please change the model ID to trained report generator and test this task:
   #{"role": "user", "content": "Now you're an expert in stock breakout detection. The direction of the breakout is upward. The resistance level is 1005.25.The seller side has more orders above the resistance level. Analyze whether this is a true or false breakout based on the known conditions, and give reasons."}

  ]
)
#print(completion.choices[0].message)
#response['choices'][0]['message']['content']
print(response.choices[0].message.content)