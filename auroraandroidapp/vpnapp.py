import uiautomator2 as u2
import random

class VPNApp():

    appname = 'com.opennet.android.ihjet903572'
    connect_text = '一键连接'
    disconnect_text = '点击断开'

    def __init__(self, d:u2.Device) -> None:
        self.d = d

    def vpn(self):
        # if not self.check_app_run():
        self.d.app_start(self.appname)
        self.d.app_wait(self.appname, front=True)
        return self.switch() if self.check_connect() else self.connect()
        # try:
        #     self.d.app_wait(self.appname, front=True)
        #     return self.switch() if self.check_connect() else self.connect()
        # except:
        #     return False
    
    def check_app_run(self) -> bool:
        """
        检查VPN APP是否运行
        """
        return True if self.appname in self.d.app_list_running() else False
    
    def check_connect(self):
        """
        检查VPN是否连接
        """
        return True if self.d(resourceId=self.appname+":id/chronometer").exists() else False
    
    def connect(self):
        """
        连接
        """
        try:
            self.d(text=self.connect_text).click(timeout=0)
            return True
        except:
            return False
    
    def disconnect(self):
        """
        断开连接
        """
        try:
            self.d(text=self.disconnect_text).click(timeout=0)
            return True
        except:
            return False
    
    def switch(self):
        """
        切换线路
        """
        current_conn_name = self.d(resourceId=self.appname+":id/last_connected_proxy").get_text()
        self.d(resourceId=self.appname+":id/last_connected_proxy").click()
        new_conn_name = None
        while True:
            new_conn_name = self.d(resourceId=self.appname+":id/proxy_name")[random.randint(0,6)].get_text()
            if current_conn_name != new_conn_name:
                self.d(text=new_conn_name).click()
                break
        return new_conn_name

if __name__ == "__main__":
    d = u2.connect('device-sn')
    vpn = VPNApp(d)
    print(vpn.vpn())
    