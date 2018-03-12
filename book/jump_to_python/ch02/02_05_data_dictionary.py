def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


"""
연관 배열(Associative array) 또는 해시(Hash)  
== 딕셔너리(Dictionary) in python
{Key1 : Value1, Key2 : Value2, Key3 : Value3 ...}
"""

dic = {"name": "pey", "phone": "0101231234", "birth": "1118"}
# {'name': 'pey', 'phone': '0101231234', 'birth': '1118'}
print(dic)
# pey
print(dic['name'])

displayTitle("딕셔너리 쌍 추가, 삭제하기")

# 1. 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
# {1: 'a', 2: 'b'}
print(a)
a['name'] = 'pey'
# {1: 'a', 2: 'b', 'name': 'pey'}
print(a)
a[3] = [1, 2, 3]
# {1: 'a', 2: 'b', 3: [1, 2, 3], 'name': 'pey'}
print(a)

displayTitle("딕셔너리를 사용하는 방법")

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
# 10
print(grade['pey'])
# 99
print(grade['julliet'])

"""
주의 사항 
1. Key는 고유함
2. key 값으로 리스트X 튜플O
"""
# key 중복
a = {1: 'a', 1: 'b'}
# {1: 'b'} // 어떤게 무시 될 지 모름
print(a)

# error
# a = {[1, 2] : 'hi'}
# print(a)

# {(1, 2): 'test'}
a = {(1, 2): 'test'}
print(a)

displayTitle("딕셔너리 관련 함수들")

# Key 리스트 만들기 (keys) : Key 값만 모아서 dict_keys 라는 객체 리턴
a = {"name": "pey", "phone": "0101231234", "birth": "1118"}
# dict_keys(['name', 'birth', 'phone']) // dict_keys 객체 리턴
print(a.keys())
# name
print(list(a.keys())[0])

# Value 리스트 만들기 (values)
# dict_values(['pey', '0101231234', '1118'])
print(a.values())
# 0101231234
print(list(a.values())[1])

# Key, Value 쌍 얻기 (items)
# dict_items([('name', 'pey'), ('phone', '0101231234'), ('birth', '1118')])
print(a.items())

# Key : Value 쌍 모두 지우기(clear)
a.clear()
# {}
print(a)

# Key로 Value 얻기 (get)
a = {"name": "pey", "phone": "0101231234", "birth": "1118"}
# pey
print(a.get('name'))
# 0101231234
print(a.get('phone'))

# error
# print(a['nokey'])
# None
print(a.get('nokey'))
# defaultValue
print(a.get('nokey', 'defaultValue'))

# 해당 Key가 딕셔너리 안에 있는지 조사 (in)
a = {"name": "pey", "phone": "0101231234", "birth": "1118"}
# True
print('name' in a)
# False
print('email' in a)
