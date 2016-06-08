# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

#Debugging print commands are left throughout the code, remove to debug

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
  
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """ 
    int_count = int(count)
    if count >= 10:
    #    print 'many'
        return 'Number of donuts: many'
    else:
    #    print int_count
        return 'Number of donuts: %d' % int_count

    raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s)<2:
    #    print 'empty'
        return ''
    else:
        ret_str = s[0:2]+s[len(s)-2:len(s)]
    #    print ret_str
        return ret_str

    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
   
    fixed_s = s[0] + s[1:len(s)].replace(s[0],"*")
    # print fixed_s
    return fixed_s
    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    c = b[0] + a[1:len(a)] \
        + " " \
        + a[0] + b[1:len(b)]
    #print c
    return c
    raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) >= 3:
        if s[len(s)-3:len(s)] == "ing":
            fin_s = s + "ly"
            return fin_s
        else:
            fin_s = s + "ing"
            return fin_s
    else:
        return s
        
    raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    not_index = s.find("not")
    bad_index = s.find("bad")

    if not_index > -1 and bad_index > not_index:
        return_string = s[0:not_index] + "good" + s[bad_index+3:len(s)]
        return return_string
    else:
        return s
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    a_half = int(round(float(len(a))/2))
    b_half = int(round(float(len(b))/2))

    end_string = a[0:a_half] + b[0:b_half] + a[a_half:len(a)] + b[b_half:len(b)]
    return end_string
    raise NotImplementedError

#donuts(10)
#donuts(50)
#donuts(1)
#donuts(2)

#both_ends("testy")
#both_ends('supderduperlong')
#both_ends('asd')
#both_ends('a')

#fix_start("babble")
#fix_start("asssaaaassaasaass")
#fix_start("super")
#fix_start("testy ttteee")

#mix_up("super", "duper")
#mix_up("testy", "random")
#mix_up("the", "purge")
#mix_up("rick", "morty")

#print verbing("halting")
#print verbing("halt")
#print verbing("as")
#print verbing("baby")

#print not_bad("not bad")
#print not_bad("this program is not really good good bad")
#print not_bad("testy test test not not not")
#print not_bad("bad bad not not")
#print not_bad("super super super")

#print front_back("abcde","wxyz")
#print front_back("Swiggity", "Swoogity")
#print front_back("Kitten", "Donut")
