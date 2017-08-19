package sele301;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;

//selenium-java-3.0.1.zipを入れて動かしたからダメだったのかも
public class TestScript{
	public static void main(String[] args) throws InterruptedException {
			System.out.println("Hello World!");
		WebDriver webDriver;
		//Chrome用ドライバを使う場合はこっち
		//System.setProperty("webdriver.chrome.driver", "C:\\home\\downloads\\chromedriver_win32\\chromedriver.exe");
		//webDriver = new ChromeDriver();    
		//Firefox用ドライバを使う場合はこっち
		System.setProperty("webdriver.gecko.driver", "/usr/local/bin/geckodriver");
		System.out.println("ブラウザを開きます");
		webDriver = new FirefoxDriver();
		/*
		 * http://www.yahoo.co.jp/ にアクセスして、
		 * <meta name="description" content="XXXX">
		 * の「XXXX」の部分を取得する
		 */
		System.out.println("指定のURLを開きます");
		String url = "http://www.yahoo.co.jp/";
		webDriver.get(url);
		String cssSelector = "meta[name=description]";
		By by = By.cssSelector(cssSelector);
		String description = webDriver.findElement(by).getAttribute("content");
		System.out.println(description);
		//終了
		System.out.println("ブラウザを閉じます");
		webDriver.quit();
	}
}