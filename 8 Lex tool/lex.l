/Definition Section/
%{
#include<stdio.h>
%}
/Rule Section/
%%
auto|double|int|struct|break|else|long|switch|case|enum|register|typedef|char|extern|return|union|continue|for|signed|void|do|if|static|while|default|goto|sizeof|volatile|const|float|short {printf("\n %s is a KEYWORD", yytext);}
[{};,()] {printf("\n %s is a SEPERATOR", yytext);}
[+-/=*%] { printf("\n %s is a OPERATOR"), yytext;}
([a-zA-Z][0-9])+|[a-zA-Z]* {printf("\n %s is a Identifier", yytext);}
.|\n ;
%%
/call the yywrap function/
int yywrap()
{
return 1;
}
int main(void)
{
yylex();
return 0;
}