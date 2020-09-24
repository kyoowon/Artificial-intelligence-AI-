from durable.lang import *

# # # with ruleset('testRS'):
# # #     # antecedent
# # #     @when_all(m.subject == 'World')
# # #     def say_hello(c):
# # #         # consequent
# # #         print('Hello {0}'.format(c.m.subject))

# # # post('test', { 'subject': 'World' })

# with ruleset('animal'):
#     # 해당 조건을 만족하는 대상 지시하는 이름
#     @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'), (m.predicate == 'lives') & (m.object == 'water') & (m.subject == c.first.subject))
#     def frog(c):
#         c.assert_fact({ 'subject': c.first.subject, 'predicate': 'is', 'object': 'frog' })
#         #사실(fact)의 추가

#     @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'), (m.predicate == 'lives') & (m.object == 'land') & (m.subject == c.first.subject))
    
#     def chameleon(c):
#         c.assert_fact({ 'subject': c.first.subject, 'predicate': 'is', 'object': 'chameleon' })

#     @when_all((m.predicate == 'eats') & (m.object == 'worms'))
#     def bird(c):
#         c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'bird' })

#     @when_all((m.predicate == 'is') & (m.object == 'frog'))
#     def green(c):
#         c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'green' })

#     @when_all((m.predicate == 'is') & (m.object == 'chameleon'))
#     def grey(c):
#         c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'grey'})

#     @when_all((m.predicate == 'is') & (m.object == 'bird'))
#     def black(c):
#         c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'black' })

#     @when_all(+m.subject) # m.subject가 한번 이상
#     def output(c):
#         print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

# assert_fact('animal', { 'subject': 'Kermit', 'predicate': 'eats', 'object': 'flies' })
# assert_fact('animal', { 'subject': 'Kermit', 'predicate': 'lives', 'object': 'water' })
# assert_fact('animal', { 'subject': 'Greedy', 'predicate': 'eats', 'object': 'flies' })
# assert_fact('animal', { 'subject': 'Greedy', 'predicate': 'lives', 'object': 'land' })
# assert_fact('animal', { 'subject': 'Tweety', 'predicate': 'eats', 'object': 'worms' })


# with ruleset('risk'):
#     @when_all(c.first << m.t == 'purchase', c.second << m.location != c.first.location)
#     def fraud(c):
#         print('이상거래 탐지 -> {0}, {1}'.format(c.first.location, c.second.location))

# post('risk', {'t': 'purchase', 'location': 'US'})
# post('risk', {'t': 'purchase', 'location': 'CA'})


with ruleset('bookstore'):
    @when_all(+m.status) #status를 갖는 것에 대해서 실행되는 규칙
    def event(c):
        print('bookstore-> Reference {0} status {1}'.format(c.m.reference, c.m.status))

    @when_all(+m.name)
    def fact(c):
        print('booksotre-> Added "{0}"'.format(c.m.name))

    @when_all(none(+m.name)) # name이 없는 것(삭제되는 것)에 추출
    def empty(c):
        print('bookstore-> No books')

#새로운 fact 추가하는 경우
assert_fact('bookstore', {'name': 'the new book', 'seller': 'bookstore', 'reference': '75323', 'price':500})

# 기존의 fact를 다시 추가하는 경우 MessageObservedError 발생
try:
    assert_fact('bookstore', {'reference': '75323', 'name': 'the new book', 'price': 500, 'seller': 'bookstore'})
except BaseException as e:
    print('Error: {0}'.format(e.message))

post('bookstore', {'reference': '75323', 'status': 'Active'})
retract_fact('bookstore', {'reference': '75323', 'name': 'the new book', 'price': 500, 'seller': 'bookstore'})