<?php 

    if(isset($_POST['btn-send']))
    {
       $UserName = $_POST['UName'];
       $Email = $_POST['Email'];
       $Subject = $_POST['Subject'];
       $Msg = $_POST['msg'];

       $email_from = $_POST ['$Email'];

       $email_body = "First Name: $FirstName.\n".
       "Last Name: $LastName.\n".
       "User Email: $Email.\n".
       "User Message: $Msg.\n";


       if(empty($UserName) || empty($Email) || empty($Subject) || empty($Msg))
       {
           header('location:index.php?error');
       }
       else
       {
           $to = "info.pipsmakerfx@gmail.com";
           $headers = "From: $email_from \r\n";

           $headers = "Reply-To: $Email \r\n";

           if(mail($to,$Subject,$Msg,$Email,$headers));
           {
               header("location:index.php?success");
           }
       }
    }
    else
    {
        header("location:index.php");
    }
?>