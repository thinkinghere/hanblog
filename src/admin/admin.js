import base from "./base";

let $error = $('meta[name=error]').attr('content');

// 有错误直接调用UIKit的消息通知
if ($error) {
  UIkit.notification({
    message: $error,
    status: 'danger',
    timeout: 1000
  });
}