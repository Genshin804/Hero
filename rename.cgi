#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
&header;

open(IN,"./data/maplog6.cgi");
@MA = <IN>;
close(IN);
foreach(@MA){
	$mapl.="<b><font color=$FCOLOR>●$MA[$m]</font></b><BR>";
	$m++;
}

print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#660033" width="700" cellspacing="5" height="509">
  <TBODY>
        <TR>
                <TD colspan="2" bgcolor="#ffffcc" height="1" align="center">
<a href=./syslog.cgi>系統公告</a>
<a href=./ilog.cgi>使用紀錄</a>
<a href=./warn.cgi>警告紀錄</a>
<a href=./rename.cgi>改名紀錄</a>
<a href=./find.cgi>打寶紀錄</a>
<a href=./sendlog.cgi>傳送紀錄</a>
<a href=./petlog.cgi>寵物轉生紀錄</a>
<a href=./mixlog.cgi>鐵匠注入奧義紀錄</a>
                </TD>
        </TR>
    <TR>
      <TD colspan="2" bgcolor="#ffffcc"><FONT style="font-size:15px" color="#666600"><改名紀錄><BR>$mapl</FONT><BR></TD>
    </TR>
  </TBODY>
</TABLE>
<BR>
</P>
</CENTER>

<hr>
EOF

&mainfooter;
exit;
