
<?php
 	//error_reporting(0);
  //<константы для обращения к контроллерам
  define('PathPerfix', 'controllers/');
  define('PathPostfix', 'Controller.php');
  //>
  include 'library/mainFunctions.php';

  //определяем с каким контроллером будем работать
  $controllerName = ucfirst($_GET['controller'])?$_GET['controller']: 'book';

  // определяем с какой функцией будем работать
  $actionName = isset($_GET['action']) ? $_GET['action'] : 'index';

  loadPage($controllerName, $actionName);
 ?>
