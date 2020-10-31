#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
require './conf_eq.cgi';
&decode;
&header;
	#&town_open;

	if($in{'mode'} eq"town_arm"){$idata="arm";$itype=0}
	elsif($in{'mode'} eq"town_pro"){$idata="pro";$itype=1}
	elsif($in{'mode'} eq"town_acc"){$idata="acc";$itype=2}
	elsif($in{'mode'} eq"r_arm"){$idata="rarearm";$itype=0}
	elsif($in{'mode'} eq"r_pro"){$idata="rarepro";$itype=1}
	elsif($in{'mode'} eq"r_acc"){$idata="rareacc";$itype=2}
	elsif($in{'mode'} eq"sp"){$itype=3}
	elsif($in{'mode'} eq"ssp") {$itype=4}
	else{$idata="arm";$itype=0}
	$item_count=0;
	if ($itype <3){
		open(IN,"./data/$idata.cgi") or exit;
		@ARM_DATA = <IN>;
		close(IN);
	
		open(IN,"./data/ability.cgi");
		@ABILITY = <IN>;
		close(IN);
	
		open(IN,"./data/towndata.cgi");
		@T_LIST = <IN>;
		close(IN);
	
	
		foreach(@COU_DATA){
			($xxcid,$xxname,$xxele,$xxgold,$xxking,$xxyaku,$xxcou,$xxmes,$xxetc)=split(/<>/);
			$country_name[$xxcid]="$xxname";
			$country_no++;
			$c_ele[$xxcid] = $xxele; 
		}
	
	
		foreach(@ARM_DATA){
			($arm_name,$arm_val,$arm_dmg,$arm_wei,$arm_ele,$arm_hit,$arm_cl,$arm_sta,$arm_type,$arm_pos)=split(/<>/);
			if ($arm_val>=10000) {
				$arm_val="<font color=blue>" . int($arm_val/10000) ."萬</font>". $arm_val%10000 ." Gold";
			} else {
				$arm_val=$arm_val . " Gold";
			}
			$sta_name="";
			#奧義
			foreach(@ABILITY){
			($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
				if($arm_sta eq $abno){
					$sta_name=$abname."(".$abcom.")";
					#exit;
					#$abcom1=$abcom;
				}
			}
			#產地
			if ($in{'mode'} eq"r_arm" || $in{'mode'} eq"r_pro" || $in{'mode'} eq"r_acc"){
			}else{
				foreach(@T_LIST){
				($zcid,$zname,$zcon,$zele,$zmoney,$zarm,$zpro,$zacc,$zind,$zs,$ztr,$zx,$zy,$zbuild,$zetc)=split(/<>/);
				($town_hp,$town_max,$town_str,$town_def,$town_dex,$town_flg)=split(/,/,$zetc);
					if ($arm_pos eq "all"){
						$buy_area="全部";
					}elsif($zcid eq $arm_pos){
						$buy_area=$zname."(".$zx.",".$zy.")";
					}
				}
			}
			$item_count++;
			$armtable.="<TR id=tr_$item_count bgcolor=white style='color: $ELE_BG[$arm_ele]'><TD><font size=2>$arm_name</font></TD><TD><font size=2>$sta_name</font></TD><TD id=td_$item_count>$ELE[$arm_ele]</TD><TD><font size=2>$arm_dmg</font></TD><TD><font size=2>$arm_wei</font></TD><TD align=right><font size=2>$arm_val</font></TD><TD align=right><font size=2>$buy_area</font></TD></TR>";
		}
	} elsif ($itype eq 3) {
	#特產
		open(IN,"./data/carm.cgi");
		@CARM = <IN>;
		close(IN);

		open(IN,"./data/ability.cgi");
		@ABILITY = <IN>;
		close(IN);
	
		open(IN,"./data/towndata.cgi");
		@T_LIST = <IN>;
		close(IN);
		#城
		foreach(@T_LIST){
		($zcid,$zname,$zcon,$zele,$zmoney,$zarm,$zpro,$zacc,$zind,$zs,$ztr,$zx,$zy,$zbuild,$zetc)=split(/<>/);
		($town_hp,$town_max,$town_str,$town_def,$town_dex,$town_flg)=split(/,/,$zetc);
			$buy_area=$zname."(".$zx.",".$zy.")";
			#特產
			foreach(@CARM){
				($arm_t,$arm_name,$arm_val,$arm_dmg,$arm_wei,$arm_ele,$arm_hit,$arm_cl,$arm_sta,$arm_type,$arm_pos)=split(/<>/);
				
				
				if ($zcid eq $arm_pos){
					if ($arm_val>=10000) {
						$arm_val="<font color=blue>" . int($arm_val/10000) ."萬</font>". $arm_val%10000 ." Gold";
					} else {
						$arm_val=$arm_val . " Gold";
					}
					#奧義
					foreach(@ABILITY){
					($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
						if($arm_sta eq $abno){
							$sta_name=$abname."(".$abcom.")";
						}
					}
					if ($arm_t eq 0){
						$arm_t="武器";
					}elsif($arm_t eq 1){
						$arm_t="防具";
					}else{
						$arm_t="飾品";
					}
					$item_count++;
					$armtable.="<TR id=tr_$item_count bgcolor=white style='color: $ELE_BG[$arm_ele]'><TD><font size=2>$arm_name</font></TD><TD><font size=2>$arm_t</font></TD><TD id=td_$item_count>$ELE[$arm_ele]</TD><TD><font size=2>$arm_dmg</font></TD><TD><font size=2>$arm_wei</font></TD><TD align=right><font size=2>$arm_val</font></TD><TD align=right><font size=2>$buy_area</font></TD></TR>";
				}

			}
			
		}
	}elsif($itype eq 4){
		foreach(@SRAR){
			$elelist.="<option value=$j>$SRAR[$j]";
			$j++;
		}
	}

	
	print <<"EOF";
<TABLE border="0" width="90%" align=center bgcolor="#000000" height="1" CLASS=TC>
  <TBODY>
    <TR>
      <TD align="center" bgcolor="$FCOLOR"><font color="#FFFFCC">
		裝備清單</font></TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc" align=center>
		<table border="0" width="100%" id="table1" cellspacing="1">
			<tr align=center>
				<form action="eqlist.cgi" method=post><td>
				
				<input type=hidden name=mode value=town_arm>
				<INPUT type=submit CLASS=FC value=商店武器>
				
				</td></form>
				<form action="eqlist.cgi" method=post><td>
				
				<input type=hidden name=mode value=town_pro>
				<INPUT type=submit CLASS=FC value=商店防具>
				
				</td></form>
				<form action="eqlist.cgi" method=post><td>
				<input type=hidden name=mode value=town_acc>
				<INPUT type=submit CLASS=FC value=商店飾品>
				
				</td></form>
				<form action="eqlist.cgi" method=post><td>
				
				<input type=hidden name=mode value=r_arm>
				<INPUT type=submit CLASS=FC value=特殊武器>
				
				</td></form>
				<form action="eqlist.cgi" method=post><td>
				
				<input type=hidden name=mode value=r_pro>
				<INPUT type=submit CLASS=FC value=特殊防具>
				
				</td></form>
				<form action="eqlist.cgi" method=post><td>
				<input type=hidden name=mode value=r_acc>
				<INPUT type=submit CLASS=FC value=特殊飾品>
				
				</td></form>
				<form action="eqlist.cgi" method=post><td>
				<input type=hidden name=mode value=sp>
				<INPUT type=submit CLASS=FC value=特產品清單>
				</td></form>
			</tr>
			<tr align=center>
				<td colspan=7 align=center>
				<INPUT type=button CLASS=FC value=全部屬性 onclick="javascript:showd('all');">　
				<INPUT type=button CLASS=FC value=$ELE[0]屬性 onclick="javascript:showd('$ELE[0]');">　
				<INPUT type=button CLASS=FC value=$ELE[1]屬性 onclick="javascript:showd('$ELE[1]');">　
				<INPUT type=button CLASS=FC value=$ELE[2]屬性 onclick="javascript:showd('$ELE[2]');">　
				<INPUT type=button CLASS=FC value=$ELE[3]屬性 onclick="javascript:showd('$ELE[3]');">　
				<INPUT type=button CLASS=FC value=$ELE[4]屬性 onclick="javascript:showd('$ELE[4]');">　
				<INPUT type=button CLASS=FC value=$ELE[5]屬性 onclick="javascript:showd('$ELE[5]');">　
				<INPUT type=button CLASS=FC value=$ELE[6]屬性 onclick="javascript:showd('$ELE[6]');">　
				<INPUT type=button CLASS=FC value=$ELE[7]屬性 onclick="javascript:showd('$ELE[7]');">
				</td>
			</tr>
		</table></TD>
    </TR>
    <TR>
      <TD align=center bgcolor="ffffff" height="48">
	<table border=0 width="100%" bgcolor=$FCOLOR CLASS=TC>
	<tr><td colspan=7 align=center><font color=ffffcc>清單</font></td></tr>
	<tr>
	<td bgcolor=ffffcc height="19" width="15%">名稱</td>
	<td bgcolor=ffffcc height="19" width="35%">奧義</td>
	<td bgcolor=ffffcc height="19" width="5%">屬性</td>
	<td bgcolor=ffffcc height="19" width="5%">威力</td>
	<td bgcolor=ffffcc height="19" width="5%">重量</td>
	<td bgcolor=ffffcc height="19" width="10%" align="right">價格</td>
	<td bgcolor=ffffcc height="19" width="15%" align="CENTER">產地</td>
	</tr>
	$armtable
	</table>
	
	<table border=0 width="90%" align=center bgcolor=$FCOLOR CLASS=TC>
	</TR></font>
	</table>
	</TR>
    </TBODY>
</TABLE>
<Script language="javascript">
function showd(ele) {
	var item_count=$item_count;
	if (ele=='all'){
		for(var i=1;i<=item_count;i++){
			document.getElementById('tr_'+i).style.display='';
		}
	} else {
		for(var i=1;i<=item_count;i++){
			if (document.getElementById('td_'+i).innerHTML==ele){
				document.getElementById('tr_'+i).style.display='';
			}else{
				document.getElementById('tr_'+i).style.display='none';
			}
		}
	};
}
</Script>
EOF
&mainfooter;
exit;
