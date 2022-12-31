#include <stdio.h>
char*s="#include <stdio.h>%cchar*s=%c%s%c;%cvoid payload(void){}int main(void){printf(s,10,34,s,34,10,10);}%c";
void payload(void){}int main(void){printf(s,10,34,s,34,10,10);}
