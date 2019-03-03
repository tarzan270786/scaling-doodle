#!/usr/bin/perl

$product_version = $ENV{'PRODUCT_VERSION'};
chomp($product_version);
print "sanity_final_${product_version}_ref.log\n";
print  "sanity_final_${product_version}_noSampleSchema_ref.log\n";

