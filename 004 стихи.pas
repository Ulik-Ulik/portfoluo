type 
fom=array [1..4]of string;
   

var
syll,strf,cnt,cnt2:integer; //syll колво слогов в строке, strf колво строф
sph:fom;

function ACC():string; 
var
quantity,quantity2:integer;
vowel,cnsnt:string;
begin
vowel:=('ааееееёёииииооооооууыэюя');
quantity:=Length(vowel);
cnsnt:=('ббббббвввгггггддджзйккклллммммнннппппппппрррррррссссттттттфхцчшшщ');
quantity2:=Length(cnsnt);
ACC:=cnsnt[random(quantity2)+1]+vowel[random(quantity)+1];
end;


procedure WRD(var cl:integer; var clv:string);
var
cnt,zakolebalo:integer;
becut:string;
begin
cnt:=1;
zakolebalo:=random(3);
while cnt<=zakolebalo do begin
                         becut:=becut+ACC;
                         //WriteLn('1',becut,'1');
                         cnt:=cnt+1;
                         end;
clv:=becut; 
//WriteLn('2',clv,'2');
cl:=zakolebalo;               
end;


procedure STROFA(s:integer;var r:fom); //получает колво слогов в строке, возвращает 4 строки
var
ck:array[1..4] of string;
g,mat:string;
cnt_1,cnt_2,nn,n,zakolebalo:integer;
begin
cnt_1:=1;
nn:=1;

mat:=ACC;
ck[1]:=mat;
ck[3]:=mat;
mat:=ACC;
ck[2]:=mat;
ck[4]:=mat;

while cnt_1<=4 do begin
                  //g:=ACC;
                  cnt_2:=1;
                  n:=random(1,2);
                  //WriteLn('$',n);
                  nn:=1;
                  while cnt_2<s do begin
                                  r[cnt_1]:=r[cnt_1]+ACC;

                                  if nn=n then begin
                                               r[cnt_1]:=r[cnt_1]+' ';
                                               n:=random(1,2);
                                               nn:=1;
                                               end
                                          else begin
                                               nn+=1;
                                               end;
                                  if s-cnt_2=1 then begin
                                                        //Writeln('-',mat[cnt_1]);
                                                        r[cnt_1]:=r[cnt_1]+ck[cnt_1]+' ';
                                                        break
                                                        end;
                                  if s-cnt_2<=3 then begin
                                                       nn:=1;
                                                       n:=s-cnt_2;
                                                       end;
                                                       

                                  cnt_2+=1;
                                  end;  

                  //WriteLn('&',cnt_1);
                  //WriteLn(r[cnt_1]);
                  cnt_1+=1;
                  end;
end;


begin
WriteLn('сколько слогов будет в строке?');
ReadLn(syll);
WriteLn('сколько будет строф?');
ReadLn(strf);

cnt:=1;
while cnt<=strf do begin
                    cnt2:=1;
                    STROFA(syll,sph);
                    while cnt2<=4 do begin
                                      writeLn(sph[cnt2],'-');
                                      sph[cnt2]:=' ';                                      
                                      cnt2+=1;
                                      end;
                                      
                    writeLn();                  
                    cnt:=cnt+1;
                    WriteLn('-------');
                    end;
end.