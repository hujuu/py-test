import org.junit.Test
import geb.junit4.GebTest

//本に載っていた書き方
class GebSampleTest extends GebTest {
	
	@Test
	void 公式サイトに行くこと() {
		go("http://www.ubisoft.co.jp/")
	}
}