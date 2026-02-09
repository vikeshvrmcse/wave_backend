from django.http import JsonResponse, HttpResponse

def home_page(reqest):
    home_information={
        'admin':'https://wave-backend-ud7m.onrender.com/admin/',
        'login':'https://wave-backend-ud7m.onrender.com/wave-backend/login/',
        'verify':'https://wave-backend-ud7m.onrender.com/wave-backend/register/',
        'resend-otp':'https://wave-backend-ud7m.onrender.com/wave-backend/register/',
        'users':'https://wave-backend-ud7m.onrender.com/wave-backend/users/',
        'users':'https://wave-backend-ud7m.onrender.com/wave-backend/video/'
    }
    # JsonResponse(home_information)

    constant='https://wave-backend-ud7m.onrender.com'

    html=HttpResponse(f'''
                      <span style="font-size:30px; color:black; text-decoratoin:none;">All Link Available Here <span style="font-size:30px;font-weight:extrabold;font-style:italic; color:orange;"> [After clicking wait 3-7 second...]</span>
                      <hr/>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/admin/">Admin Link</a> <span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/admin/]</span><div>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/register/">Register Link</a><span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/register/]</span><div>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/verify-otp/">Verify OTP Link</a><span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/verify-otp/]</span><div>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/resend-otp/">Resend OTP Link</a><span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/resend-otp/]</span><div>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/login/">Login Link</a><span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/login/]</span><div>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/users/">Show All Users Link</a><span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/users/]</span><div>
                      <div><a style="font-size:30px; color:black; text-decoratoin:none;" href="{constant}/wave-backend/videos/">Show All Videos Link</a><span style="font-size:30px;font-weight:bold;font-style:italic; color:purple;"> [{constant}/wave-backend/videos/]</span><div>
                      
                      ''')
    return html