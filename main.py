import sys
import butlerian
import lightcontroller as LightController

_JOB_NAME_ENV = 'PI_LIT_JOB_NAME'
_APP_NAME_ENV = 'PI_LIT_APP_NAME'


class MissingParameterException(Exception):
    def __init__(self, message):
        super(MissingParameterException, self).__init__(message)


if __name__ == '__main__':
    import os

    job_name = os.getenv(_JOB_NAME_ENV, 'build-apps-apk')
    app_name = os.getenv(_APP_NAME_ENV, 'tables2')

    if not job_name or not app_name:
        raise MissingParameterException("Error: environment variables {} and {} must be set."
                                        .format(_JOB_NAME_ENV, _APP_NAME_ENV))

    jenkins = butlerian.JenkinsApi()
    job = jenkins.get_job(job_name, app_name)
    if job.builds:
        controller = LightController.LightController()
        # Get most recent build.
        build = job.builds[0]
        print 'Build:\t{}\tbuilding={}\tresult={}'.format(
            build.full_display_name, build.building, build.result)
        print 'Color:\t',

        if build.building:
            os.system('omxplayer -o local ~/Downloads/test.mp3')
            controller.set_status(LightController.Status.BUILDING)
            print 'yellow'  # Change LED color here
            pass
        elif build.result == 'SUCCESS':
            os.system('omxplayer -o local ~/Downloads/test.mp3')
            controller.set_status(LightController.Status.PASSING)
            print 'green'   # Change LED color here
            pass
        elif build.result == 'FAILURE':
            os.system('omxplayer -o local ~/Downloads/test.mp3')
            controller.set_status(LightController.Status.FAILING)
            print 'red'     # Change LED color here
            pass
    else:
        print 'No build results found'
        sys.stderr.write(job.get_pretty_xml())
