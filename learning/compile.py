# everything is code object!
print(compile('sum([1, 2, 3])', '', 'single'))
exec(compile('sum([1, 2, 3])', '', 'single'))