<?php
include 'ChromePhp.php';
ChromePhp::log('Hits contact_me.php');

// Check for empty fields
if(empty($_POST['name'])      ||
   empty($_POST['email'])     ||
   empty($_POST['phone'])     ||
   empty($_POST['message'])   ||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
   echo "No arguments Provided!";

	ChromePhp::warn('Not working');
   return false;
   } else {
$name = strip_tags(htmlspecialchars($_POST['name']));
$email_address = strip_tags(htmlspecialchars($_POST['email']));
$phone = strip_tags(htmlspecialchars($_POST['phone']));
$message = strip_tags(htmlspecialchars($_POST['message']));
   
// Create the email and send the message
//$to = 'sampunchfyp@gmail.com'; // Add your email address inbetween the '' replacing yourname@yourdomain.com - This is where the form will send a message to.
//$email_subject = "Website Contact Form:  $name";
//$email_body = "You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: $name\n\nEmail: $email_address\n\nPhone: $phone\n\nMessage:\n$message";
//$headers = "From: test@noreply.google.com\n"; // This is the email address the generated message will be from. We recommend using something like noreply@yourdomain.com.
//$headers .= "Reply-To: $email_address";   




$to = "116355346@umail.ucc.ie";
$subject = "Few Looseners";
$txt = "Mon we go to the rock";
$headers = "From: webmaster@example.com" . "\r\n" .
"CC: somebodyelse@example.com";


if(mail($to,$subject,$txt,$headers)){
	ChromePhp::warn('Hup the lads mon we go to the rock');
	ChromePhp::log('=========================');
	ChromePhp::log($to);
	ChromePhp::log($subject);
	ChromePhp::log($txt);
	ChromePhp::log($headers);
	return true; 
} else {
	ChromePhp::warn('Email Not Sent');
	ChromePhp::log('=========================');
	ChromePhp::log($to);
	ChromePhp::log($subject);
	ChromePhp::log($txt);
	ChromePhp::log($headers);
	return false;
}
	
	

}        
?>
