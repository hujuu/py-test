import org.openqa.selenium.By;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebDriver;

//selenium-java-2.53.1.zipを入れて動かしたからダメだったのかも
public class SampleScript{
	
	public static void main(String[] args){
		WebDriver driver = new FirefoxDriver();
		driver.get("https://github.com/");
		driver.quit();
	}
}