package no.bekk;

import no.bekk.guestbook.GuestBook;
import org.apache.wicket.protocol.http.WebApplication;
import org.apache.wicket.settings.IMarkupSettings;

/**
 * Application object for your web application. If you want to run this application without deploying, run the Start class.
 *
 */
public class WicketApplication extends WebApplication {
    /**
     * Constructor
     */
    public WicketApplication() {
    }

    protected void init() {
        super.init();
        IMarkupSettings markupSettings = getMarkupSettings();
        markupSettings.setDefaultMarkupEncoding("UTF-8");
        markupSettings.setStripWicketTags(true);
        mountBookmarkablePage("/guestbook", GuestBook.class);
    }

    /**
     * @see org.apache.wicket.Application#getHomePage()
     */
    public Class<HomePage> getHomePage() {
        return HomePage.class;
    }

}
