#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
require './conf_eq.cgi';

&decode;

if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("資料傳輸有誤，<a href='./login.cgi'>請重新登入</a>。"); }
if ($in{'id'} eq "2930"){
        &verchklog("town.cgi,$in{'mode'}");
}
if($in{'mode'} eq"equip"){require './status/equip.pl';&equip;}
elsif($in{'mode'} eq"equip2"){require './status/equip2.pl';&equip2;}
elsif($in{'mode'} eq"equip3"){require './status/equip3.pl';&equip3;}
elsif($in{'mode'} eq"status"){require './status/status.pl';&status;}
elsif($in{'mode'} eq"change"){require './status/change.pl';&change;}
elsif($in{'mode'} eq"change2"){require './status/change2.pl';&change2;}
elsif($in{'mode'} eq"renkin"){require './status/renkin.pl';&renkin;}
elsif($in{'mode'} eq"renkin2"){require './status/renkin2.pl';&renkin2;}
elsif($in{'mode'} eq"name_change"){require './status/name_change.pl';&name_change;}
elsif($in{'mode'} eq"name_change2"){require './status/name_change2.pl';&name_change2;}
elsif($in{'mode'} eq"prof_edit"){require './status/prof_edit.pl';&prof_edit;}
elsif($in{'mode'} eq"prof_write"){require './status/prof_write.pl';&prof_write;}
elsif($in{'mode'} eq"skill"){require './status/skill.pl';&skill;}
elsif($in{'mode'} eq"skill2"){require './status/skill2.pl';&skill2;}
elsif($in{'mode'} eq"skill3"){require './status/skill3.pl';&skill3;}
elsif($in{'mode'} eq"sk_set"){require './status/sk_set.pl';&sk_set;}
elsif($in{'mode'} eq"sk_set2"){require './status/sk_set2.pl';&sk_set2;}
elsif($in{'mode'} eq"con_renew"){require './status/con_renew.pl';&con_renew;}
elsif($in{'mode'} eq"tec_set"){require './status/tec_set.pl';&tec_set;}
elsif($in{'mode'} eq"tec_set2"){require './status/tec_set2.pl';&tec_set2;}
elsif($in{'mode'} eq"data_change"){require './status/data_change.pl';&data_change;}
elsif($in{'mode'} eq"data_change2"){require './status/data_change2.pl';&data_change2;}
elsif($in{'mode'} eq"money_send"){require './status/money_send.pl';&money_send;}
elsif($in{'mode'} eq"money_send2"){require './status/money_send2.pl';&money_send2;}
elsif($in{'mode'} eq"item_send"){require './status/item_send.pl';&item_send;}
elsif($in{'mode'} eq"item_send2"){require './status/item_send2.pl';&item_send2;}
elsif($in{'mode'} eq"item_send3"){require './status/item_send3.pl';&item_send3;}
elsif($in{'mode'} eq"item_send4"){require './status/item_send4.pl';&item_send4;}
elsif($in{'mode'} eq"item_send5"){require './status/item_send5.pl';&item_send5;}
elsif($in{'mode'} eq"getabp"){require './status/getabp.pl';&getabp;}
elsif($in{'mode'} eq"getabp2"){require './status/getabp2.pl';&getabp2;}
elsif($in{'mode'} eq"chat"){require './status/chat.pl';&chat;}
elsif($in{'mode'} eq"hero"){require './status/hero.pl';&hero;}
elsif($in{'mode'} eq"backup"){require './status/backup.pl';&backup;}
elsif($in{'mode'} eq"outpet"){require './status/outpet.pl';&outpet;}
else{&error2("資料傳送錯誤,請重新選擇。");}
exit;
