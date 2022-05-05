KEYWORDS = ["alignas","alignof","and","and_eq","asm","atomic_cancel","atomic_commit","atomic_noexcept","auto","bitand","bitor","bool","break","case","catch","char","char8_t","char16_t","char32_t","class","compl","concept","const","consteval","constexpr","constinit","const_cast","continue","co_await","co_return","co_yield","decltype","default","delete","do","double","dynamic_cast","else","enum","explicit","export","extern","false","float","for","friend","goto","if","inline","int","long","mutable","namespace","new","noexcept","not","not_eq","nullptr","operator","or","or_eq","private","protected","public","reflexpr","register","reinterpret_cast","requires","return","short","signed","sizeof","static","static_assert","static_cast","struct","switch","synchronized","template","this","thread_local","throw","true","try","typedef","typeid","typename","union","unsigned","using","virtual","void","volatile","wchar_t","while","xor","xor_eq"]

PREPROCESSORS = ['#define', '#undef', '#include', '#if', '#ifdef', '#ifndef', '#else', '#elif', '#elifdef', '#elifndef', '#endif', '#line', '#error', '#pragma']

SYMBOLS = ['=', '+=', '/=', '*=', '-=', '==', '!=', '<', '<=', '>', '>=', '&', '&', '&&', '|', '||', '!', '>>', '>>>', '<<', '<<<' ,  ';', '{', '}', '[', ']', '(', ')']

# header files
# identifires
# keywords
# symbol
# preprocessor
# comments

code = []

with open('7 Lexical analyzer/a.cpp') as f:
    code = f.readlines()

inlineComment = False
blockComment = False

output = []
for line in code:
    for word in line.split():
        if word == '//':
            break
        if word in KEYWORDS:
            output.append([word, "KEYWORD"])
        elif word in SYMBOLS:
            output.append([word, "SYMBOL"])
        elif word in PREPROCESSORS:
            output.append([word, "PREPROCESSOR"])
        elif word.isdigit():
            output.append([word, "CONSTANT"])
        elif word[0] == '<' and word[-1] == '>':
            output.append([word, "FILE DIRECTIVE"])
        elif word[0] == '"':
            nword = word[1:-1]
            output.append([nword])
        elif word[0] == '\\':
            break
        else:
            output.append([word, "IDENTIFIER"]) 

for i in output:
    for j in i:
        print(j, end=" ")
    print()

print(output)