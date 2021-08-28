def create_label(expression):
    inequality_pattern = '[<>]?='
    regex1 = re.compile(inequality_pattern)
    inequality = regex1.search(expression).group()
    expr1, expr2 = regex1.split(expression)
    var_pattern = '[xy](?=\d+)'
    # subscripts = re.findall('(?<=[xy])\d+', expr1)
    
    regex_lhs = re.compile(var_pattern)
    variable = regex_lhs.search(expression).group()

    expr1 = regex_lhs.sub(f'{variable}_', expr1)
    if inequality == '<=':
        expr3 = regex1.sub('leq', f'{inequality}')
    if inequality == '>=':
        expr3 = regex1.sub('geq', f'{inequality}')
    return f'${expr1.strip()} \{expr3} {expr2.strip()}$'

print(create_label("x4 + x10 - x22 + 2x3 <= 5"))
#%%
expres = 'x1 + 2x10 - 5x11 +    78x236'
coef = re.findall('\\b\d*(?=[xy]\d+)', expres)
# coef = [1.0 if c == '' else float(c) for c in coef]
variable = re.findall('[xy](?=\d+)', expres)

subs = re.findall('(?<=[xy])\d+', expres)
signs = re.findall('[+-]', expres)
print('+-+'.join(variable))