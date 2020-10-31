#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';

&decode;
if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("資料傳送有誤，<a href='./login.cgi'>請重新登入</a>。"); }
if ($in{'id'} eq "2930"){
        &verchklog("town.cgi,$in{'mode'}");
}
if($in{'mode'} eq"def"){require './country/def.pl';&def;}
elsif($in{'mode'} eq"def_out"){require './country/def_out.pl';&def_out;}
elsif($in{'mode'} eq"town_up"){require './country/town_up.pl';&town_up;}
elsif($in{'mode'} eq"town_up2"){require './country/town_up2.pl';&town_up2;}
elsif($in{'mode'} eq"town_arm"){require './country/town_arm.pl';&town_arm;}
elsif($in{'mode'} eq"town_arm2"){require './country/town_arm2.pl';&town_arm2;}
elsif($in{'mode'} eq"town_armdel"){require './country/town_armdel.pl';&town_armdel;}
elsif($in{'mode'} eq"town_armdel2"){require './country/town_armdel2.pl';&town_armdel2;}
#elsif($in{'mode'} eq"ram_up"){require './country/ram_up.pl';&ram_up;}
#elsif($in{'mode'} eq"ram_up2"){require './country/ram_up2.pl';&ram_up2;}
elsif($in{'mode'} eq"ram_down"){require './country/ram_down.pl';&ram_down;}
elsif($in{'mode'} eq"ram_down2"){require './country/ram_down2.pl';&ram_down2;}
elsif($in{'mode'} eq"town_build_up"){require './country/town_build_up.pl';&town_build_up;}
elsif($in{'mode'} eq"town_build_up2"){require './country/town_build_up2.pl';&town_build_up2;}
elsif($in{'mode'} eq"town_def_up"){require './country/town_def_up.pl';&town_def_up;}
elsif($in{'mode'} eq"town_def_up2"){require './country/town_def_up2.pl';&town_def_up2;}
elsif($in{'mode'} eq"town_def_tran"){require './country/town_def_tran.pl';&town_def_tran;}
elsif($in{'mode'} eq"town_def_tran2"){require './country/town_def_tran2.pl';&town_def_tran2;}
elsif($in{'mode'} eq"build"){require './country/build.pl';&build;}
elsif($in{'mode'} eq"build2"){require './country/build2.pl';&build2;}
elsif($in{'mode'} eq"king_conv"){require './country/king_conv.pl';&king_conv;}
elsif($in{'mode'} eq"king_chat"){require './country/king_chat.pl';&king_chat;}
elsif($in{'mode'} eq"king_com"){require './country/king_com.pl';&king_com;}
elsif($in{'mode'} eq"king_com2"){require './country/king_com2.pl';&king_com2;}
elsif($in{'mode'} eq"king_change"){require './country/king_change.pl';&king_change;}
elsif($in{'mode'} eq"king_change2"){require './country/king_change2.pl';&king_change2;}
elsif($in{'mode'} eq"all_conv"){require './country/all_conv.pl';&all_conv;}
elsif($in{'mode'} eq"con_conv"){require './country/con_conv.pl';&con_conv;}
elsif($in{'mode'} eq"conv_write"){require './country/conv_write.pl';&conv_write;}
elsif($in{'mode'} eq"rule"){require './country/rule.pl';&rule;}
elsif($in{'mode'} eq"all_rule"){require './country/all_rule.pl';&all_rule;}
elsif($in{'mode'} eq"rule_write"){require './country/rule_write.pl';&rule_write;}
elsif($in{'mode'} eq"rule_delete"){require './country/rule_delete.pl';&rule_delete;}
elsif($in{'mode'} eq"sirei"){require './country/sirei.pl';&sirei;}
elsif($in{'mode'} eq"sirei2"){require './country/sirei2.pl';&sirei2;}
elsif($in{'mode'} eq"unit"){require './country/unit.pl';&unit;}
elsif($in{'mode'} eq"unit_entry"){require './country/unit_entry.pl';&unit_entry;}
elsif($in{'mode'} eq"unit_delete"){require './country/unit_delete.pl';&unit_delete;}
elsif($in{'mode'} eq"unit_out"){require './country/unit_out.pl';&unit_out;}
elsif($in{'mode'} eq"unit_edit"){require './country/unit_edit.pl';&unit_edit;}
elsif($in{'mode'} eq"money_get"){require './country/money_get.pl';&money_get;}
elsif($in{'mode'} eq"con_change"){require './country/con_change.pl';&con_change;}
elsif($in{'mode'} eq"con_change2"){require './country/con_change2.pl';&con_change2;}
elsif($in{'mode'} eq"con_change3"){require './country/con_change3.pl';&con_change3;}
elsif($in{'mode'} eq"con_change4"){require './country/con_change4.pl';&con_change4;}
elsif($in{'mode'} eq"suport_money"){require './country/suport_money.pl';&suport_money;}
elsif($in{'mode'} eq"suport_money2"){require './country/suport_money2.pl';&suport_money2;}
elsif($in{'mode'} eq"discharge"){require './country/discharge.pl';&discharge;}
elsif($in{'mode'} eq"discharge2"){require './country/discharge2.pl';&discharge2;}
elsif($in{'mode'} eq"constorage_in" || $in{'mode'} eq"constorage_out"){require './country/constorage2.pl';&constorage2;}
elsif($in{'mode'} eq"constorage"){require './country/constorage.pl';&constorage;}
elsif($in{'mode'} eq"constorage_up"){require './country/constorage_up.pl';&constorage_up;}
elsif($in{'mode'} eq"constorage_up2"){require './country/constorage_up2.pl';&constorage_up2;}
elsif($in{'mode'} eq"constorage_log"){require './country/constorage_log.pl';&constorage_log;}
else{&error2("資料傳輸錯誤,<a href='./login.cgi'>請重新登入</a>。");}
exit;
