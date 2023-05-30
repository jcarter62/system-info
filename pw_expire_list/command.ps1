#
# Generate list of users and number of days until password expires.
#
# Ref: https://www.webservertalk.com/check-password-expires-in-active-directory/
#
Import-Module ActiveDirectory
$MaxPwdAge = (Get-ADDefaultDomainPasswordPolicy).MaxPasswordAge.Days
$expiredDate = (Get-Date).addDays(-$MaxPwdAge)
#Set the number of days until you would like to begin notifing the users. -- Do Not Modify --
#Filters for all users who's password is within $date of expiration.
$NonExpiredUsers = Get-ADUser -Filter {
    (PasswordLastSet -gt $expiredDate) -and
    (PasswordNeverExpires -eq $false) -and
    (Enabled -eq $true)
} -Properties PasswordNeverExpires, PasswordLastSet, Mail |
  select samaccountname, PasswordLastSet, Mail,
  @{
    name = "DaysUntilExpired";
    Expression = {$_.PasswordLastSet - $ExpiredDate | select -ExpandProperty Days}
  } |
  Sort-Object PasswordLastSet

$ExpiredUsers = Get-ADUser -Filter {
    (PasswordLastSet -lt $expiredDate) -and
    (PasswordNeverExpires -eq $false) -and
    (Enabled -eq $true)
} -Properties PasswordNeverExpires, PasswordLastSet, Mail |
  select samaccountname, PasswordLastSet, Mail,
  @{
    name = "DaysUntilExpired";
    Expression = {$_.PasswordLastSet - $ExpiredDate | select -ExpandProperty Days}
  } |
  Sort-Object PasswordLastSet

$AllUsers = $NonExpiredUsers + $ExpiredUsers

$AllUsers | ConvertTo-Json
