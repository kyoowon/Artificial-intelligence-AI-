from durable.lang import *


with ruleset('light'):
    
    @when_all(+m.subject)
    def output(c):
        if (c.m.And == 'I want to Save-energy'):
            print('Condition : {0} {1} {2}. {3}'.format(c.m.subject, c.m.predicate, c.m.object, c.m.And))
        elif (c.m.object == 'AM' or c.m.object == 'PM'):
            print("Condition : {0} {1} after {2} {3} o'clock.".format(c.m.subject, c.m.predicate, c.m.object, c.m.object2))
        else :
            print('Condition : {0} {1} {2}.'.format(c.m.subject, c.m.predicate, c.m.object))



    # 날씨에 대한 규칙
    @when_all((m.subject == 'Wheather') & (m.predicate == 'is') & (m.object == 'Sunny'))
    def w_sunny(c):
        num = 20
        print('Recommendation : use {0} and {1} {2}.'.format('LED','{0}%'.format(num), 'brightness'))

    @when_all((m.subject == 'Wheather') & (m.predicate == 'is') & (m.object == 'Cludy'))
    def w_Cludy(c):
        num = 60
        print('Recommendation : use {0} and {1} {2}.'.format('tricuspid bulb', '{0}%'.format(num),'brightness'))

    @when_all((m.subject == 'Wheather') & (m.predicate == 'is') & (m.object == 'Rain'))
    def w_Cludy(c):
        num = 100
        print('Recommendation : use {0} and {1} {2}.'.format('tricuspid bulb', '{0}%'.format(num),'brightness'))
        

    @when_all((m.subject == 'Wheather') & (m.predicate == 'is') & (m.object == 'Snow'))
    def w_Cludy(c):
        num = 80
        print('Recommendation : use {0} and {1} {2}.'.format('tricuspid bulb', '{0}%'.format(num),'brightness'))


    # 시간에 대한 규칙
    @when_any((m.object == 'AM') & (m.object2 > 10), (m.object == 'PM') & (m.object2 <= 6))
    def W_early(c):
        num = 60
        print('Recommendation : use {0} and {1} {2}.'.format('LED','{0}%'.format(num), 'brightness'))

    @when_any((m.object == 'AM') & (m.object2 <= 10), (m.object == 'PM') & (m.object2 > 6))
    def W_Late(c):
        num = 80
        print('Recommendation : use {0} and {1} {2}.'.format('tricuspid bulb','{0}%'.format(num), 'brightness'))


    # 사람의 활동에 대한 규칙
    @when_all((m.subject == 'People') & (m.predicate == 'need') & (m.object == 'light atmosphere'))
    def w_Cludy(c):
        num = 40
        print('Recommendation : use {0} and {1} {2}.'.format('fluorescent lamp', '{0}%'.format(num),'brightness'))

    @when_all((m.subject == 'People') & (m.predicate == 'need') & (m.object == 'concentrate'))
    def w_sunny(c):
        num = 100
        print('Recommendation : use {0} and {1} {2}.'.format('incandescent lamp', '{0}%'.format(num),'brightness'))


    # 실내 활동에 대한 규칙
    @when_all((m.subject == 'People') & (m.predicate == 'active in') & (m.object == 'the room'))
    def w_Cludy(c):
        num = 60
        print('Recommendation : use {0} and {1} {2}.'.format('LED', '{0}%'.format(num),'brightness'))

    @when_all((m.subject == 'People') & (m.predicate == 'not active in') & (m.object == 'the room'))
    def w_sunny(c):
        num = 0
        print('Recommendation : use {0} and {1} {2}.'.format('LED', '{0}%'.format(num),'brightness'))


# tricuspid bulb, fluorescent lamp, incandescent lamp, LED
# 100%, 80%, 60%, 40%, 20% 
# wheather, time zone, energy_safe, active_people

assert_fact('light', {'subject': 'Wheather', 'predicate': 'is', 'object': 'Sunny'})
assert_fact('light', {'subject': 'Wheather', 'predicate': 'is', 'object': 'Sunny', 'And' : 'I want to Save-energy'})

assert_fact('light', {'subject': 'Wheather', 'predicate': 'is', 'object': 'Cludy'})
assert_fact('light', {'subject': 'Wheather', 'predicate': 'is', 'object': 'Rain'})
assert_fact('light', {'subject': 'Wheather', 'predicate': 'is', 'object': 'Snow'})
assert_fact('light', {'subject': 'Wheather', 'predicate': 'is', 'object': 'Cludy', 'And' : 'I want to Save-energy'})

assert_fact('light', {'subject': 'Time zone', 'predicate': 'is used', 'object': 'AM', 'object2': 11})
assert_fact('light', {'subject': 'Time zone', 'predicate': 'is used', 'object': 'PM', 'object2': 8})

assert_fact('light', {'subject': 'People', 'predicate': 'need', 'object': 'concentrate'})
assert_fact('light', {'subject': 'People', 'predicate': 'need', 'object': 'light atmosphere'})

assert_fact('light', {'subject': 'People', 'predicate': 'active in', 'object': 'the room'})
assert_fact('light', {'subject': 'People', 'predicate': 'not active in', 'object': 'the room'})