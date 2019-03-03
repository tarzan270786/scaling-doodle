#!/usr/bin/perl 
use List::Util qw(first);
use strict ;
use warnings ;
my %hash = ();
sub diagnose() {
	my ($enterValue,$key1,$line) = @_ ;
	#print "Values passed $enterValue : $key1\n";
	open(FHR1,"<" ,"errorList.txt") or die "Some problem with opening the file $!\n";
	while (my $line = <FHR1>) {
		chomp($line);
		next if ($line =~ /^\// or $line =~ /^$/) ;
		my ($key , $value ) = split(/:/ , $line,2 );
		my @values = split(/\,/ , $value);
		@{$hash{$key}} =  @values  ; #store the array of errors in hash
	
	       	}
		#print "found in hash \n" if first {$_ eq  $enterValue} @{$hash{$key1}} ;
		close (FHR1);
		#if (grep {$hash{$_} eq $enterValue} keys %hash)  {
		if (first {$_ eq $enterValue} @{$hash{$key1}}){	 
			#print "Inside sav \n" ;
	          generate_logs($key1,"sav",$line);
		  #print "returning from sav \n"
	           }
	        else {
			#print "Inside dif \n"; 
	           generate_logs($key1,"dif",$line) ;
		   #print "returning from dif \n"
	         }


}

sub generate_logs {
	 my $strng1 = "$_[0] module logs show up some  errors.See below  for more  details\n";
	 my $extn = $_[1] ;
	 system("perl -e 'print \"$strng1\"' >> $_[0].$extn");
	 system("sed -i'.orig' -e '/module/a $_[2]'  $_[0].$extn");
	 #print "returning from generate logs \n";
    }


    #&diagnose("abc","TDE");
sub error_check {
my $generate = (split/\./, (split/\//, $_[0])[-1])[-2];
print uc($generate),"\n" ;
#my $b= "pdbcs_pdb_install_22775_8305.log";
my $b = $_[0];
my $db_support_logs=`grep -E "^ORA-|^SP2-|^ERROR|^FATAL|^SEVERE" $b`;
#print "ERRORS IN $b => $db_support_logs" ;  
if($db_support_logs)
{
my $str1="file $b got few errors\n";                                                                                                                                                       
open(FL, ">> $_[1].tmp");                                                                                                                                                       
print FL "$str1\n";                                                                                                                                                                     
print FL "$db_support_logs\n";                                                                                                                                                          
close(FL);                                                                                                                                                                                                                                                                                    
}
my $line ;
if ( -s "$_[1].tmp") {
open(FHR ,"<" , "$_[1].tmp") or die "Some error $!\n" ;
while(  $line =  <FHR>) {
chomp($line); 
#print "$line\n" ;
if (($line  =~ m/(^ORA-\d{5}|^SP2-\d{4})/)){
my $error = $& ;
print "Error is :: $error \n" ;
my $key = $_[1];
&diagnose("$error" , "$key",$line);         
#print "After return from diagnose\n"; 
}
if(($_[1] eq "CEN_objectstore") || ($_[1] eq "POD1_obj_store"))                                                                                                                         
        {                                                                                                                                                                              
	system ("mv $_[1].sav $_[1].dif");                                                                                                                      
       } 
}
}
else	{                                                                                                                                                                                       
	system("touch $_[1].suc");                                                                                                                                                      
	}        

close(FHR);
}

#&error_check("tdeexec_CEN.log","TDEconfig");

#error_check("T_WORK/oraunzip_exec_CEN.log");
#error_check("T_WORK/ssl_walletexec_CEN.log");

error_check("CEN_TDECONFIG.tmp","TDEconfig");
