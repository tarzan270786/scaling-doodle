#!/usr/bin/perl
use File::Compare;
print "Inside compare module";

my @files = grep{!/\ref.log$/} glob(Users/rrshanke/Documents/sanity_final*[^ref].log);
print "@files\n";
foreach $file(@files){

if ($file =~ /DWCSSEED/) {
	$san_ref = "sanity_final_DWCSSEED_ref.log";
	}
elsif ($file =~ /OLTPSEED/) {
	$san_ref = "sanity_final_OLTPSEED_ref.log";
	}
else {
	$san_ref ="sanity_final_pdb_ref.log" ; 
} 
# Comparing the log file now 
if(File::Compare::compare("$file","$san_ref") == 0)
{
system("touch $T_WORK/sanitycheck_{file}.suc");\
}
else
{
system("touch $T_WORK/sanitycheck_{$file}.sav");
print "sanitycheck_{$file}.sav is present . Some sanity has failed . Refer WORK\n";
}

#write_to_tlgfile("sanitycheck.sav in T_WORK means some of the sanities could have failed.To refer sanity_final.log in WORK");


}
