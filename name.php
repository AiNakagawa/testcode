<?php
echo "<!DOCTYPE html>\n";
echo "<html lang=\"jp\">\n";
echo "<head>\n";
echo "    <meta charset=\"UTF-8\">\n";
echo "   <title>test_flask</title>\n";
echo "</head>\n";
echo "<body >\n";
echo "    <form action='/result'>\n";
echo "        <p>{{message}}</p>\n";
echo "        <input type=\"text\" name=\"field\">\n";
echo "        <button type=\"submit\" formmethod=\"POST\">送信</button>\n";
echo "    </form>\n";
echo "</body>\n";
echo "</html>\n";
echo "";
?>
