import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons';

import '../scss/admin.scss'  // 导入scss文件
// loads the Icon plugin
UIkit.use(Icons);

// components can be called from the imported UIkit reference
UIkit.notification('123 Hello world. 123 haha');  // 通知
export default UIkit; // 导出UIkit 在其他文件中可以引用