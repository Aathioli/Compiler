%{ 
int idn = 0;
int cons = 0 ;  
%} 
  
%option noyywrap
%% 
   
  
"int"|"float" {printf("\t keywords : %s", yytext);}   

[a-zA-Z_][a-zA-Z0-9_]* {idn++;printf("\t identifier : %s", yytext);} 

[0-9]*"."[0-9]+ {cons++;printf("\t float : %s", yytext);}  

[0-9]+ {cons++;printf("\t integer : %s", yytext);}                        
  
.    ;
%% 
   
   
int main() 
  
{ 
      
    yylex();
      
    printf("\n total no. of identifier = %d\n", idn);   
    printf("\n total no. of constants = %d\n", cons);
       
} 