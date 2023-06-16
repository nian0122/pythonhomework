"""编写一个应用程序，找出字符串“2018俄罗斯世界杯，一届没有中国队的世界杯，一届属于中国企业的世界杯。”中，以“世界杯”结尾的单词，并显示出匹配的位置。运行效果如下：
[7, 19, 32]
"""
"""import re
res="2018俄罗斯世界杯，一届没有中国队的世界杯，一届属于中国企业的世界杯。"
search=re.compile(r'')"""
import re
s = '2018俄罗斯世界杯，一届没有中国队的世界杯，一届属于中国企业的世界杯。'
pattern =re.compile(r'\.*世界杯')
result = pattern.finditer(s)
indices = [match.start()for match in result]
print(indices)
