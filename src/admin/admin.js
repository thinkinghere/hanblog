import UIkit from './base'; // 引入base

let $error = $('meta[name=error]').attr('content');

// 有错误直接调用UIKit的消息通知
if ($error) {
  UIkit.notification({
    message: $error,
    status: 'danger',
    timeout: 1000
  });
}

// 点击切换tab
$('.uk-tab a').on('click', (event)  => {
  let $this = $(event.currentTarget)[0];
  window.location.replace($this.href);
});
