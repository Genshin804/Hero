#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
	&decode;
	&header;
	
	#列數
	$col=9;
	#行數
	$line=7;
	#１ページに表示する數
	$pre=$col*$line;

	$page=$in{'page'};
	$nextpage=$page+1;
	$frontpage=$page-1;
	$first=$page*$pre+1;
	$last=$first+$pre-1;
	if($last>$CHARAIMG){$last=$CHARAIMG;}
	print"<center><table CLASS=TC width=900><tr><td colspan=15 align=center><font color=$FCOLOR2 size=4>圖案一覧</font></td></tr>";
	for($i=$first;$i<=$last;$i++){
		if(($i)%$col eq 1){
			print"<tr>";
		}
		print"<td align=center bgcolor=$FCOLOR2><img src=$IMG/chara/$i.gif><br><font size=2>No.$i</font></td>";
		if($i%$col eq $col){
			print"</tr>";
		}
	}

	print"<tr><td bgcolor=$FCOLOR2 colspan=15 align=center>";
	if($page>0){
		print"<form action=icon.cgi method=POST><input type=hidden name=page value=$frontpage><input type=submit CLASS=FC value=前一頁></form>";
	}
	if($i<$CHARAIMG){
		print"<form action=icon.cgi method=POST><input type=hidden name=page value=$nextpage><input type=submit CLASS=FC value=下一頁></form>";
	}
	print"</td></tr>";
	print"</table>";
	$con_no=0;
	
	print"</table></center><BR>";
&mainfooter;
exit;
