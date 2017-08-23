package sele351;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;

//selenium-java-3.5.1.zipを入れて動かしたらいけた
public class SeleniScript{
	public static void main(String[] args) throws InterruptedException {
		WebDriver webDriver;
		//Chrome用ドライバを使う場合はこっち
		//System.setProperty("webdriver.chrome.driver", "C:\\home\\downloads\\chromedriver_win32\\chromedriver.exe");
		//webDriver = new ChromeDriver();    
		//Firefox用ドライバを使う場合はこっち
		//ドライバをの直接指定もできる
		//System.setProperty("webdriver.gecko.driver", "/usr/local/bin/geckodriver");
		System.out.println("ブラウザを開きます");
		webDriver = new FirefoxDriver();
		
		System.out.println("指定のURLを開きます");
		String url = "http://www.yahoo.co.jp/";
		webDriver.get(url);
		String cssSelector = "meta[name=description]";
		By by = By.cssSelector(cssSelector);
		String description = webDriver.findElement(by).getAttribute("content");
		//サイトのディスクリプションを表示
		System.out.println(description);
		//終了
		System.out.println("ブラウザを閉じます");
		webDriver.quit();
	}
}