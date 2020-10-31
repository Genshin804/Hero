#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
        &decode;
        &header;
#one_piece118.gif
#bleach188.gif
#naruto389.gif
#        &ext_open;
        $IMGT="http://s658.photobucket.com/albums/uu305/machineliao";
		if($in{'sel'} eq"one_pice"){
			$CHARAIMG=117;
		}elsif($in{'sel'} eq"bleach"){
			$CHARAIMG=187;
		}elsif($in{'sel'} eq"naruto"){
			$CHARAIMG=388;
                }elsif($in{'sel'} eq"fma"){
                        $CHARAIMG=84;
		}else{
		}
        #列數
        $col=4;
        #行數
        $line=3;
        #１ページに表示する數
        $pre=$col*$line;

        $page=$in{'page'};
        $nextpage=$page+1;
        $frontpage=$page-1;
        $first=$page*$pre+1;
        $last=$first+$pre-1;
        if($last>$CHARAIMG){$last=$CHARAIMG;}
        print"<center><table CLASS=TC width=900><tr><td colspan=4 align=center><font color=$FCOLOR2 size=4>動態頭像一覧</font></td></tr>";
        print"<tr><td colspan=4 align=center><a href=\"?sel=one_pice\"><font color=$FCOLOR2 size=2>海賊王</font></a>　<a href=\"?sel=naruto\"><font color=$FCOLOR2 size=2>火影忍者</font></a>　<a href=\"?sel=bleach\"><font color=$FCOLOR2 size=2>死神</font></a>　<a href=\"?sel=fma\"><font color=$FCOLOR2 size=2>鋼之鍊金術師</font></a></td></tr>";
        for($i=$first;$i<=$last;$i++){
                if(($i)%$col eq 1){
                        print"<tr>";
                }
                print"<td align=center bgcolor=$FCOLOR2><img src=$IMGT/chara/$in{'sel'}$i.gif><br><font size=2>No.$i</font></td>";
                if($i%$col eq $col){
                        print"</tr>";
                }
        }

        print"<tr><td bgcolor=$FCOLOR2 colspan=15 align=center>";
        if($page>0){
                print"<form action=act_icon.cgi method=POST><input type=hidden name=sel value=$in{'sel'}><input type=hidden name=page value=$frontpage><input type=submit CLASS=FC value=前一頁></form>";
        }
        if($i<$CHARAIMG){
                print"<form action=act_icon.cgi method=POST><input type=hidden name=sel value=$in{'sel'}><input type=hidden name=page value=$nextpage><input type=submit CLASS=FC value=下一頁></form>";
        }
        print"</td></tr>";
        print"</table>";
        $con_no=0;

        print"</table></center><BR>";
&mainfooter;
exit;
