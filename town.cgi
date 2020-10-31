#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
require './conf_pet.cgi';

&decode;
if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("資料傳輸有誤，<a href='./login.cgi'>請重新登入</a>。"); }
if($in{'mode'} eq"inn"){require './town/inn.pl';&inn;}
elsif($in{'mode'} eq"rshop"){require './town/rshop.pl';&rshop;}
elsif($in{'mode'} eq"rbuy"){require './town/rbuy.pl';&rbuy;}
elsif($in{'mode'} eq"quest"){require './town/quest.pl';&quest;}
elsif($in{'mode'} eq"quest2"){require './town/quest2.pl';&quest2;}
elsif($in{'mode'} eq"hinn"){require './town/hinn.pl';&hinn;}
elsif($in{'mode'} eq"hinn2"){require './town/hinn2.pl';&hinn2;}
elsif($in{'mode'} eq"hinn3"){require './town/hinn3.pl';&hinn3;}
elsif($in{'mode'} eq"event"){require './town/event.pl';&event;}
elsif($in{'mode'} eq"event2"){require './town/event2.pl';&event2;}
elsif($in{'mode'} eq"arm" || $in{'mode'} eq"pro" || $in{'mode'} eq"acc" || $in{'mode'} eq"item"){require './town/shop.pl';&shop;}
elsif($in{'mode'} eq"buy"){require './town/buy.pl';&buy;}
elsif($in{'mode'} eq"sell"){require './town/sell.pl';&sell;}
elsif($in{'mode'} eq"fshop"){require './town/fshop.pl';&fshop;}
elsif($in{'mode'} eq"sshop"){require './town/sshop.pl';&sshop;}
elsif($in{'mode'} eq"sshop2"){require './town/sshop2.pl';&sshop2;}
elsif($in{'mode'} eq"sshop3"){require './town/sshop3.pl';&sshop3;}
elsif($in{'mode'} eq"sshop4"){require './town/sshop4.pl';&sshop4;}
elsif($in{'mode'} eq"fex"){require './town/fex.pl';&fex;}
elsif($in{'mode'} eq"fbid"){require './town/fbid.pl';&fbid;}
elsif($in{'mode'} eq"fget"){require './town/fget.pl';&fget;}
elsif($in{'mode'} eq"s_shop"){require './town/s_shop.pl';&s_shop;}
elsif($in{'mode'} eq"s_buy"){require './town/s_buy.pl';&s_buy;}
elsif($in{'mode'} eq"arena"){require './town/arena.pl';&arena;}
elsif($in{'mode'} eq"entry_can"){require './town/entry_can.pl';&entry_can;}
elsif($in{'mode'} eq"battle_entry"){require './town/battle_entry.pl';&battle_entry;}
elsif($in{'mode'} eq"battle_entry2"){require './town/battle_entry2.pl';&battle_entry2;}
elsif($in{'mode'} eq"battle_entry_list"){require './town/battle_entry_list.pl';&battle_entry_list;}
elsif($in{'mode'} eq"battle_entry_history"){require './town/battle_entry_history.pl';&battle_entry_history;}
elsif($in{'mode'} eq"bank"){require './town/bank.pl';&bank;}
elsif($in{'mode'} eq"banka"||$in{'mode'} eq"bankh"||$in{'mode'} eq"bankall"||$in{'mode'} eq"bankhall"){require './town/bank2.pl';&bank2;}
elsif($in{'mode'} eq"storage"){require './town/storage.pl';&storage;}
elsif($in{'mode'} eq"storage_in" || $in{'mode'} eq"storage_out" || $in{'mode'} eq"storage_sort" || $in{'mode'} eq"storage_sort_name"){require './town/storage2.pl';&storage2;}
elsif($in{'mode'} eq"storage_up"){require './town/storage_up.pl';&storage_up;}
elsif($in{'mode'} eq"petup"){require './town/petup.pl';&petup;}
elsif($in{'mode'} eq"petup2"){require './town/petup2.pl';&petup2;}
elsif($in{'mode'} eq"rpetup"){require './town/rpetup.pl';&rpetup;}
elsif($in{'mode'} eq"rpetup2"){require './town/rpetup2.pl';&rpetup2;}
elsif($in{'mode'} eq"mix"){require './town/mix.pl';&mix;}
elsif($in{'mode'} eq"mix2"){require './town/mix2.pl';&mix2;}
elsif($in{'mode'} eq"mixbook"){require './town/mixbook.pl';&mixbook;}
elsif($in{'mode'} eq"mixbook2"){require './town/mixbook2.pl';&mixbook2;}
elsif($in{'mode'} eq"mix_change"){require './town/mix_change.pl';&mix_change;}
elsif($in{'mode'} eq"mix_change2"){require './town/mix_change2.pl';&mix_change2;}
elsif($in{'mode'} eq"action"){require './town/action.pl';&action;}
elsif($in{'mode'} eq"action2"){require './town/action2.pl';&action2;}
elsif($in{'mode'} eq"action3"){require './town/action3.pl';&action3;}
else{&error2("資料傳輸有誤。");}
exit;
