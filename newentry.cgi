#!/usr/bin/perl

#################################################################
#   【免責事項】                                                #
#    このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
#    また設置に関する質問はサポート掲示板にお願いいたします。   #
#    直接メールによる質問は一切お受けいたしておりません。       #
#################################################################

require './jcode.pl';
require './sub.cgi';
require './conf.cgi';

&decode;

if($in{'mode'} eq 'ATTESTATION') { require './attestation.cgi';&attestation; }
elsif($in{'mode'} eq 'set_entry') { require './attestation.cgi';&set_entry; }
else{ require './attestation.cgi';&attestation;}

exit;
