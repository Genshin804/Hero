#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';

&decode;
if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("資料傳輸有誤，<a href='./login.cgi'>請重新登入</a>。"); }
if($in{'mode'} eq"move"){require './etc/move.pl';&move;}
elsif($in{'mode'} eq"move2"){require './etc/move2.pl';&move2;}
elsif($in{'mode'} eq"inv"){require './etc/inv.pl';&inv;}
elsif($in{'mode'} eq"inv2"){require './etc/inv2.pl';&inv2;}
elsif($in{'mode'} eq"setkey"){require './etc/setkey.pl';&setkey;}
elsif($in{'mode'} eq"setkey2"){require './etc/setkey2.pl';&setkey2;}
elsif($in{'mode'} eq"mode_change"){require './etc/mode_change.pl';&mode_change;}
elsif($in{'mode'} eq"mode_change2"){require './etc/mode_change2.pl';&mode_change2;}
else{&error2("資料傳送錯誤,請重新選擇。");}
exit;
