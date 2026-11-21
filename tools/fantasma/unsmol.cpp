// unsmol: decompress smol data (pokeemerald-expansion's compresSmol format) from a ROM offset.
// usage: unsmol ROM OFFSET OUT
#include "compressAlgo.h"
#include <fstream>
int main(int argc, char **argv) {
    std::ifstream f(argv[1], std::ios::binary); std::vector<unsigned char> rom((std::istreambuf_iterator<char>(f)), {});
    size_t off = strtoul(argv[2], 0, 0);
    auto U = [&](size_t i) { size_t o = off + 4 * i; return (unsigned)rom[o] | rom[o+1] << 8 | rom[o+2] << 16 | (unsigned)rom[o+3] << 24; };
    CompressedImage img; std::vector<unsigned int> hv = {U(0), U(1)};
    readNewHeader(&hv, &img); img.headers = hv;
    bool lo = isModeLoEncoded(img.mode), sym = isModeSymEncoded(img.mode);
    size_t i = 2;
    if (lo) for (int k = 0; k < 3; k++) img.loFreqs[k] = U(i++);
    if (sym) for (int k = 0; k < 3; k++) img.symFreqs[k] = U(i++);
    if (lo || sym) for (size_t k = 0; k < img.bitreamSize; k++) img.tANSbits.push_back(U(i++));
    size_t bo = off + 4 * i;
    if (!sym) { for (size_t k = 0; k < img.symSize; k++) img.symVec.push_back(rom[bo + 2*k] | rom[bo + 2*k + 1] << 8); bo += 2 * img.symSize; }
    if (!lo) for (size_t k = 0; k < img.loSize; k++) img.loVec.push_back(rom[bo + k]);
    std::vector<unsigned short> out = decodeImageShort(&img);
    std::ofstream o(argv[3], std::ios::binary);
    for (auto v : out) { o.put(v & 0xff); o.put(v >> 8); }
    fprintf(stderr, "mode %d raw %zu got %zu\n", img.mode, img.rawNumBytes, out.size()*2);
}
