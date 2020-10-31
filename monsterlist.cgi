#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
&header;
        open(IN,"./data/monster.cgi");
        @MON_DATA = <IN>;
        close(IN);
        
        open(IN,"./data/tec.cgi");
        @TEC = <IN>;
        close(IN);

        open(IN,"./data/ability.cgi");
        @ABILITY = <IN>;
        close(IN);
        $ELEVEL[1]="草原";
        $ELEVEL[2]="沼地";
        $ELEVEL[3]="森林";
        $ELEVEL[4]="高塔";
	$ELEVEL[5]="廢城";
	$ELEVEL[6]="禁地";
	$ELEVEL[99]="神獸";
        $no1=1;
        $mtable="";

        foreach(@MON_DATA){
                ($ename,$eab,$etec,$esk,$e_ex,$e_gold,$etype,$elv)=split(/<>/);
                ($ehp,$emp,$estr,$evit,$eint,$efai,$edex,$eagi,$eele)=split(/,/,$eab);
                ($etec1,$etec2,$etec3,$emprate,$ehprate)=split(/,/,$etec);
                ($etec_name[0],$etec_str[0],$etec_hit[0],$etec_mp[0],$etec_ab[0],$etec_sta[0],$etec_class[0]) = split(/<>/,$TEC[$etec1]);
                ($etec_name[1],$etec_str[1],$etec_hit[1],$etec_mp[1],$etec_ab[1],$etec_sta[1],$etec_class[1]) = split(/<>/,$TEC[$etec2]);
                ($etec_name[2],$etec_str[2],$etec_hit[2],$etec_mp[2],$etec_ab[2],$etec_sta[2],$etec_class[2]) = split(/<>/,$TEC[$etec3]);
		($abils[0],$abils[1])=split(/,/,$esk);
                $esk="";
                $ej=0;
		foreach(@abils){
        	        foreach(@ABILITY){
       		                ($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
	                                if ($abno eq "$abils[$ej]"){
                               		        $esk.="$abname";
						if($abils[$ej+1]){$esk.="<BR><font color=green>";}
                       		                last;
               		                }
       		                }
			$ej++;
			}
		if ($ehprate) {
			$ehprate="<br>HP:$ehprate\%";
		}
		if ($emprate){
			$emprate="<br>MP:$emprate\%";
		}
                $mtable.="<tr id=tr_$no1 style='COLOR: #555555' bgColor=white style='font-size=10pt'><td id=td_$no1>$ELEVEL[$elv]</td><td>$ename</td><td>$ehp</td><td>$emp</td><td>$estr</td><td>$evit</td><td>$eint</td><td>$efai</td><td>$edex</td><td>$eagi</td><td>$ELE[$eele]</td><td>$etec_name[0]</td><td>$etec_name[1]$emprate</td><td>$etec_name[2]$ehprate</td><td>$esk</td></tr>";
                $no1++;
        }
	$mon_count=$no1-1;
        print <<"EOF";

<table class="TC" height="1" width="90%" align="center" bgColor="#000000" border="0" id="table2">
	<tr>
		<td align="middle" bgColor="#883300"><font color="#FFFFCC">地圖清單</font></td>
	</tr>
	<tr>
		<td align="middle" bgColor="#ffffcc">
		<table id="table3" cellSpacing="1" width="100%" border="0">
			<tr align="middle">
					<td><input class="FC" type="button" value="草原" onclick="javascript:showd('草原');"> </td>
					<td><input class="FC" type="button" value="沼地" onclick="javascript:showd('沼地');"> </td>
					<td><input class="FC" type="button" value="森林" onclick="javascript:showd('森林');"> </td>
					<td><input class="FC" type="button" value="高塔" onclick="javascript:showd('高塔');"></td>
                                        <td><input class="FC" type="button" value="廢城" onclick="javascript:showd('廢城');"></td>
                                        <td><input class="FC" type="button" value="禁地" onclick="javascript:showd('禁地');"></td>
                                        <td><input class="FC" type="button" value="神獸" onclick="javascript:showd('神獸');"></td>

				</form>
			</tr>
		</table>
		</td>
	</tr>
	<tr>
		<td align="middle" bgColor="#ffffff" height="48">
		<table class="TC" width="100%" bgColor="#883300" border="0" id="table4">
			<tr>
				<td align="middle" colSpan="15"><font color="#ffffcc">怪物清單</font></td>
			</tr>
			<tr style='font-size=10pt'>
				<td width="2%" bgColor="#ffffcc" height="19">　</td>
				<td width="10%" bgColor="#ffffcc" height="19">名稱</td>
				<td width="7%" bgColor="#ffffcc" height="19">HP</td>
				<td width="6%" bgColor="#ffffcc" height="19">MP</td>
				<td width="6%" bgColor="#ffffcc" height="19">力量</td>
				<td width="6%" bgColor="#ffffcc" height="19">生命力</td>
				<td width="4%" bgColor="#ffffcc" height="19">智力</td>
				<td width="4%" bgColor="#ffffcc" height="19">精神</td>
				<td width="4%" bgColor="#ffffcc" height="19">運氣</td>
				<td width="4%" bgColor="#ffffcc" height="19">速度</td>
				<td width="5%" bgColor="#ffffcc" height="19">屬性</td>
				<td width="10%" bgColor="#ffffcc" height="19">技能１</td>
				<td width="10%" bgColor="#ffffcc" height="19">技能２</td>
				<td width="10%" bgColor="#ffffcc" height="19">技能３</td>
				<td align="middle" width="16%" bgColor="#ffffcc" height="19">奧義</td>
			</tr>
			$mtable
		</table>
		</td>
	</tr>
</table>
<Script language="javascript">
function showd(mapname) {
        var item_count=$mon_count;
                for(var i=1;i<=item_count;i++){
                        if (document.getElementById('td_'+i).innerHTML==mapname){
                                document.getElementById('tr_'+i).style.display='';
                        }else{
                                document.getElementById('tr_'+i).style.display='none';
                        }
		}
}
showd('草原');
</Script>

EOF
&mainfooter;
exit;

