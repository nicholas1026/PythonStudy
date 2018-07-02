def build_profile( first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_ name'] = first
    profile['last_ name'] = last
    for key, value in user_info. items():
        profile[ key] = value
    return profile

user_profile = build_profile('yunfei', 'xi', city='shanghai', country='china',sex='male',age=30)
print(user_profile)
