import asyncio
import requests

async def fun1():
    url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1b67055b-392b-423a-ae8b-58f8e53701bf/dfjkl4t-ed340ca6-6c2c-4ef0-9e5e-8798508b4718.jpg/v1/fit/w_828,h_1324,q_70,strp/goku_4k_wallpaper_hd__by_manankamra07_dfjkl4t-414w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQwMCIsInBhdGgiOiJcL2ZcLzFiNjcwNTViLTM5MmItNDIzYS1hZThiLTU4ZjhlNTM3MDFiZlwvZGZqa2w0dC1lZDM0MGNhNi02YzJjLTRlZjAtOWU1ZS04Nzk4NTA4YjQ3MTguanBnIiwid2lkdGgiOiI8PTg3NiJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.TobbMLGaeG92FQWkyBOtz13X-09HU1UiPjOwzpUpRDo"
    r = requests.get(url)
    open("goku1.jpg", "wb").write(r.content)
    print("Image downloaded successfully!")
async def fun2():
    url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/76a4ea45-e203-480b-8f72-6cc4f94659c3/djyjj5q-48a91b37-b20a-47db-9a81-b0fd6f290719.jpg/v1/fill/w_1210,h_660,q_70,strp/dragon_ball_wallpapers___hd_fan_art_ai_by_mcnokaut_djyjj5q-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzc2YTRlYTQ1LWUyMDMtNDgwYi04ZjcyLTZjYzRmOTQ2NTljM1wvZGp5amo1cS00OGE5MWIzNy1iMjBhLTQ3ZGItOWE4MS1iMGZkNmYyOTA3MTkuanBnIiwiaGVpZ2h0IjoiPD02OTkiLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS53YXRlcm1hcmsiXSwid21rIjp7InBhdGgiOiJcL3dtXC83NmE0ZWE0NS1lMjAzLTQ4MGItOGY3Mi02Y2M0Zjk0NjU5YzNcL21jbm9rYXV0LTQucG5nIiwib3BhY2l0eSI6OTUsInByb3BvcnRpb25zIjowLjQ1LCJncmF2aXR5IjoiY2VudGVyIn19.q9Z52Y0cQ3htpuE7YlHyWhsKjl4R82hK8knBZEmfk5s"
    r = requests.get(url)
    open("goku2.jpg", "wb").write(r.content)
    print("Image downloaded successfully!")
async def fun3():
    url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/76a4ea45-e203-480b-8f72-6cc4f94659c3/djysq6h-7d97e96b-746a-4582-b904-38318ed17783.jpg/v1/fill/w_1210,h_660,q_70,strp/dragon_ball_fan_art_wallpaper_hd_ai_ultra_2025_by_mcnokaut_djysq6h-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzc2YTRlYTQ1LWUyMDMtNDgwYi04ZjcyLTZjYzRmOTQ2NTljM1wvZGp5c3E2aC03ZDk3ZTk2Yi03NDZhLTQ1ODItYjkwNC0zODMxOGVkMTc3ODMuanBnIiwiaGVpZ2h0IjoiPD02OTkiLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS53YXRlcm1hcmsiXSwid21rIjp7InBhdGgiOiJcL3dtXC83NmE0ZWE0NS1lMjAzLTQ4MGItOGY3Mi02Y2M0Zjk0NjU5YzNcL21jbm9rYXV0LTQucG5nIiwib3BhY2l0eSI6OTUsInByb3BvcnRpb25zIjowLjQ1LCJncmF2aXR5IjoiY2VudGVyIn19.fLBnw935hV_k8WbwWtS2EKaW1cNJcgYS1_KFQ2blx1g"
    r = requests.get(url)
    open("goku3.jpg", "wb").write(r.content)
    print("Image downloaded successfully!")

async def main():
    await asyncio.gather(fun1(), fun2(), fun3())        
